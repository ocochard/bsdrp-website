# bsdrp.net Makefile (BSD make)
#
# Targets:
#   build     - mkdocs build --strict (output in ./site/)
#   serve     - mkdocs serve on ${SERVE_ADDR} (local preview)
#   deploy    - run ./deploy.sh (build + sftp mirror to OVH)
#   deploy-n  - dry-run upload (./deploy.sh -n)
#   clean     - remove ./site/

SITE_DIR=	site
SERVE_ADDR=	0.0.0.0:8081

.PHONY: build serve deploy deploy-n clean

build:
	mkdocs build --strict

serve:
	mkdocs serve --dev-addr ${SERVE_ADDR}

deploy:
	./deploy.sh

deploy-n:
	./deploy.sh -n

clean:
	rm -rf ${SITE_DIR}
