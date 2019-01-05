setup:
	# Install pipenv
	pip install pipenv

	# Install python packages in Pipfile
	pipenv install --dev

test:
	pipenv run python manage.py test