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

migrate:
	$(MANAGE) migrate --noinput

run: ARGS=0.0.0.0:8000
run:
	$(MANAGE) runserver $(ARGS)

docker-build:
	docker build -t demo-app/ricardokirkner .

docker-run:
	docker run -it demo-app/ricardokirkner

start:
	python manage.py migrate --noinput
	python manage.py runserver 0.0.0.0:8000
