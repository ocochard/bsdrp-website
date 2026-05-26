#!/bin/sh
# deploy.sh - build the bsdrp.net mkdocs site and upload it over SFTP.
#
# Credentials are read from ~/.netrc (chmod 600), NOT from this script.
# The matching entry is:
#
#     machine ftp.cluster010.ovh.net
#         login bsdrp
#         password ...
#
# Usage:  ./deploy.sh            real upload
#         ./deploy.sh -n         dry-run (lftp prints what it would do)

set -eu

# --- Config ---------------------------------------------------------------
REMOTE_HOST="ftp.cluster010.ovh.net"
REMOTE_USER="bsdrp"
REMOTE_DIR="www"
LOCAL_DIR="site"

REPO_DIR=$(cd -- "$(dirname -- "$0")" && pwd)
LOG_DIR="${HOME}/bin/log"
LOG_FILE="${LOG_DIR}/deploy_bsdrp.net.log"

DRY_RUN=""
if [ "${1:-}" = "-n" ] || [ "${1:-}" = "--dry-run" ]; then
	DRY_RUN="--dry-run"
fi

# --- Pre-flight checks ----------------------------------------------------
cd "${REPO_DIR}"

if [ ! -f mkdocs.yml ]; then
	echo "deploy.sh: mkdocs.yml not found in ${REPO_DIR}" >&2
	exit 1
fi

if ! command -v mkdocs >/dev/null 2>&1; then
	echo "deploy.sh: mkdocs not in PATH" >&2
	exit 1
fi

if ! command -v lftp >/dev/null 2>&1; then
	echo "deploy.sh: lftp not in PATH" >&2
	exit 1
fi

if [ ! -f "${HOME}/.netrc" ]; then
	echo "deploy.sh: ${HOME}/.netrc not found - cannot authenticate" >&2
	exit 1
fi

# .netrc must be chmod 600 or lftp/ssh will refuse to read it
netrc_mode=$(stat -f '%Lp' "${HOME}/.netrc" 2>/dev/null || stat -c '%a' "${HOME}/.netrc")
if [ "${netrc_mode}" != "600" ]; then
	echo "deploy.sh: ${HOME}/.netrc must be chmod 600 (currently ${netrc_mode})" >&2
	exit 1
fi

mkdir -p "${LOG_DIR}"

# --- Build ----------------------------------------------------------------
echo "deploy.sh: building site (strict mode)..."
rm -rf "${LOCAL_DIR}"
mkdocs build --strict

if [ ! -d "${LOCAL_DIR}" ] || [ -z "$(ls -A "${LOCAL_DIR}")" ]; then
	echo "deploy.sh: build produced no output in ${LOCAL_DIR}" >&2
	exit 1
fi

# mkdocs does not copy .htaccess (Apache redirects from the old DokuWiki URLs)
# into the build output. Copy it in so it ends up on the server and so the
# --delete mirror does not wipe it.
if [ -f .htaccess ]; then
	cp .htaccess "${LOCAL_DIR}/.htaccess"
fi

# --- Upload ---------------------------------------------------------------
# We use lftp with the sftp:// protocol. lftp reads ~/.netrc automatically
# when no password is given in the `open` line.
#
# mirror -R           reverse mirror (local -> remote)
# --delete            remove remote files that no longer exist locally
# --parallel=4        4 concurrent transfers
# --verbose=2         per-file progress
# --exclude-glob ...  never touch these even if they exist remotely
echo "deploy.sh: uploading to sftp://${REMOTE_HOST}${REMOTE_DIR} ${DRY_RUN:+(dry-run)}"

lftp -c "
set cmd:fail-exit true;
set net:max-retries 2;
set net:reconnect-interval-base 5;
set sftp:auto-confirm yes;
set sftp:connect-program \"ssh -a -x -o PubkeyAuthentication=no -o PreferredAuthentications=password\";
debug -o ${LOG_FILE} 3;
open sftp://${REMOTE_USER}@${REMOTE_HOST};
cd ${REMOTE_DIR};
lcd ${REPO_DIR}/${LOCAL_DIR};
mirror -R --delete --parallel=4 --verbose=2 ${DRY_RUN} \
	--exclude-glob sessions/ \
	--exclude-glob HTTPCS55470.html \
	--exclude-glob LiveSearchSiteAuth.xml \
	--exclude-glob google0a2bf5e42d3355b1.html \
	--exclude-glob ppxfkyy3gk.txt \
	--exclude-glob y_key_e97cb3e97accaeb1.html \
	. .;
"

echo "deploy.sh: done."
