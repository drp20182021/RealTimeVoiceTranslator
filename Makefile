# Install project dependencies from requirements.txt
install:
	pip install -r requirements.txt

# Remove temporary and cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .mypy_cache
	rm -rf .pytest_cache

# Run unit tests
test:
	python -m unittest discover -s tests
