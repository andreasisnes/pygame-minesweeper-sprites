ENV=pipenv

.PHONY: init test egg publish clean

all: init test egg publish

init:
	@$(ENV) sync

test:
	@$(ENV) run pytest --cov=minesweeper tests

egg:
	@$(ENV) run python setup.py sdist bdist_wheel

publish:
	@$(ENV) run twine check dist/*
	@$(ENV) run twine upload dist/*

clean:
	@find . -type f -name ".mypy_cache" -print0 | xargs -r0 -- rm -r
	@find . -type d -name ".pytest_cache" -print0 | xargs -r0 -- rm -r
	@find . -type d -name "__pycache__" -print0 | xargs -r0 -- rm -r
	@find . -type d -name "*.pyc" -print0 | xargs -r0 -- rm -r
	@rm -rf *.egg-info build dist .coverage