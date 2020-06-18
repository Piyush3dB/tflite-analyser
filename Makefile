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

pipup:
	sudo python3.6 -m pip install --upgrade pip

venv: info
	virtualenv -p /usr/bin/python3.6 venv


clean_venv: info
	rm -rf ./venv
	
fbs: info
	rm -rf schema.fbs;
	wget https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/schema/schema.fbs;
	flatc --version;
	flatc --python schema.fbs;

clean:
	rm -rf ./schema

clean_venv:
	rm -rf ./venv

all: info
