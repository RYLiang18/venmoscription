venv/setup:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip pip-tools
	touch venv/setup

venv/touchfile: venv/setup requirements.txt
	./venv/bin/pip install -r requirements.txt
	touch venv/touchfile

requirements.txt: requirements.in
	./venv/bin/pip-compile --upgrade requirements.in

.PHONY: format
format:
	./venv/bin/black --target-version py313 venmoscription