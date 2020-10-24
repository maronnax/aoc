.venv/bin/python3.7:
	python3.7 -m venv --prompt $(shell basename $(shell pwd)) .venv
	.venv/bin/pip install -U setuptools wheel pip pip-tools
	.venv/bin/pip install -r requirements.txt


install: .venv/bin/python3.7
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install -e .
