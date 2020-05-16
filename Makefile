dir = $(shell pwd)

init: create-env install

create-env:
	python3 -m virtualenv venv

install:
	test -d venv || virtualenv venv
	. ${dir}/venv/bin/activate; pip install -r requirements.txt

clean:
    rm -rf venv
    find -iname "*.pyc" -delete
