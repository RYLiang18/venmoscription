venv/setup:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip pip-tools
	touch venv/setup

requirements.txt: requirements.in
	./venv/bin/pip-compile --upgrade requirements.in