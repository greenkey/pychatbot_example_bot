.PHONY: test help init run
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys
for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

init: ## installs all the requirements for dev env
	pip install --upgrade pip
	pip install -r requirements.txt

test: ## run tests quickly with the default Python
	pytest tests.py
	
run: ## run the bot
	python run.py