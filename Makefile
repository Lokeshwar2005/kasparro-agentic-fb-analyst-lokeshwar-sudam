VENV_NAME = .venv
PYTHON = $(VENV_NAME)/bin/python
SRC_DIR = src

.PHONY: setup run test lint clean

setup: $(VENV_NAME)
	@echo "Setting up virtual environment and installing dependencies..."
	$(PYTHON) -m pip install -r requirements.txt
	@echo "Setup complete. To activate: source $(VENV_NAME)/bin/activate"

$(VENV_NAME):
	python3 -m venv $(VENV_NAME)

run:
	@if [ -z "54240OPENAI_API_KEY" ]; then 		echo "ERROR: OPENAI_API_KEY environment variable is not set. Using simulation."; 	fi
	@echo "Executing analysis..."
	$(PYTHON) run.py 'Analyze ROAS drop in the last week.'

test:
	@echo "Running Evaluator tests..."
	$(PYTHON) -m unittest discover tests

clean:
	@echo "Cleaning up environment..."
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete
	rm -rf reports/* logs/*
