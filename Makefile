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

.PHONY: help build serve deploy deploy-n clean

help:
	@echo "Available targets:"
	@echo "  help      - show this message"
	@echo "  build     - mkdocs build --strict (output in ./${SITE_DIR}/)"
	@echo "  serve     - mkdocs serve on ${SERVE_ADDR} (local preview)"
	@echo "  deploy    - run ./deploy.sh (build + sftp mirror to OVH)"
	@echo "  deploy-n  - dry-run upload (./deploy.sh -n)"
	@echo "  clean     - remove ./${SITE_DIR}/"

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
