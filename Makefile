ENV=pipenv


test:
	@$(ENV) run pytest --cov=minesweeper tests