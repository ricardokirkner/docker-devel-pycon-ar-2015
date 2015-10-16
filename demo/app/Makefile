ENV = env
MANAGE = $(PYTHON) manage.py
PIP = $(ENV)/bin/pip
PYTHON = $(ENV)/bin/python
VIRTUALENV = virtualenv


bootstrap: $(ENV)

$(ENV):
	$(VIRTUALENV) $(ENV)
	$(PIP) install -r requirements.txt

clean:
	find . -name '*.pyc' -delete
	rm -f .coverage

full-clean: clean
	rm -rf $(ENV)

manage:
	$(MANAGE) $(ARGS)

run: ARGS=0.0.0.0:8000
run:
	$(MANAGE) runserver $(ARGS)

