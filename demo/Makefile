DOCKER_COMPOSE = $(ENV)/bin/docker-compose
ENV = env
PIP = $(ENV)/bin/pip

SERVICE ?= 


help:
	@echo "help  -- print this help"
	@echo "build -- build docker environment"
	@echo "start -- start docker stack"
	@echo "stop  -- stop docker stack"
	@echo "env   -- create a virtualenv"
	@echo "clean -- clean all artifacts"

$(ENV): $(ENV)/bin/activate

build: .build

start: build
	$(DOCKER_COMPOSE) up -d $(SERVICE)

stop:
	$(DOCKER_COMPOSE) stop $(SERVICE)

clean: clean-docker clean-env
	@rm -rf .build

# helpers

$(ENV)/bin/activate: build-requirements.txt
	@test -d $(ENV) || virtualenv $(ENV)
	@$(PIP) install -r build-requirements.txt
	@touch $(ENV)/bin/activate

.build: $(ENV) docker-compose.yml
	@$(DOCKER_COMPOSE) build $(SERVICE)
	@touch .build

clean-docker:
	$(DOCKER_COMPOSE) rm --force

clean-env:
	@rm -rf $(ENV)


.PHONY: help build start stop clean clean-docker clean-env
