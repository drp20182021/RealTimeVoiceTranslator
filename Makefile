PYTHON = python
PIP = pip
FD_DIR = frontend
TEST_DIR = tests

install:
	@$(PIP) install -r requirements.txt
	@$(PYTHON) -m unidic download

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.pyc" -delete
	@find . -name "*.pyo" -delete

run_app:
	streamlit run $(FD_DIR)/main.py

test_config:
	@$(PYTHON) $(TEST_DIR)/test_config.py

test_transcribe:
	@$(PYTHON) $(TEST_DIR)/test_transcribe.py

test_translate:
	@$(PYTHON) $(TEST_DIR)/test_translate.py

test_synthesize:
	@$(PYTHON) $(TEST_DIR)/test_synthesize.py
