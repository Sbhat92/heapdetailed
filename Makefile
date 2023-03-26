
#########
# LINTS #
#########
lint:  ## run static analysis with flake8
	python -m black --check heapdetailed setup.py
	python -m flake8 heapdetailed setup.py

# Alias
lints: lint

format:  ## run autoformatting with black
	python -m black heapdetailed/ setup.py

# alias
fix: format

check:  ## check assets for packaging
	check-manifest -v

# Alias
checks: check

annotate:  ## run type checking
	python -m mypy ./heapdetailed

#########
# TESTS #
#########
test: ## clean and run unit tests
	python -m pytest -v heapdetailed/tests

coverage:  ## clean and run unit tests with coverage
	python -m pytest -v heapdetailed/tests --cov=heapdetailed --cov-branch --cov-fail-under=75 --cov-report term-missing

# Alias
tests: test