requirements:
	pip install -r requirements.txt

validate_quality:
	pylint crypto/usermanagement/; \
	pep8 crypto
