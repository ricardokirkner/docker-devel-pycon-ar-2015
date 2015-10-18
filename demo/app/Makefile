ENV = env
GUNICORN = $(ENV)/bin/gunicorn
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

run: ARGS=-b 0.0.0.0:8000
run:
	$(MANAGE) collectstatic --noinput
	$(GUNICORN) $(ARGS) project.wsgi:application

docker-build:
	docker build -t demo-app/ricardokirkner .

docker-run:
	docker run -it demo-app/ricardokirkner

start:
	python manage.py migrate --noinput
	python manage.py collectstatic --noinput
	honcho start
