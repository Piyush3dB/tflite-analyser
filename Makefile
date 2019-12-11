THIS_FILE := $(lastword $(MAKEFILE_LIST))
UNAME := $(shell uname)
FLATC_INFO := $(shell flatc --version)
# 
# EDIT THESE
#
FLATC_PLACE=PLACE

#ifeq ($(UNAME), Linux)
#    @echo "is Linux"
#else
#	@echo "is Mac"
#endif


#
# DO NOT EDIT
#

.DEFAULT_GOAL := all
.PHONY: info


info:
	@echo "   "
	@echo "==INFORMATION=================================="
	@echo "    UNAME = $(UNAME)"
	@echo "    FLATC = $(FLATC_INFO)"
	@echo "   "

venv: info
	sudo python3.6 -m pip install --upgrade pip
	virtualenv -p /usr/bin/python3.6 venv
	source ./venv/bin/activate
	pip install pipenv
	pipenv install

clean_venv: info
	rm -rf ./venv
	
fbs_api: info
	./download_schema.sh


all: info
