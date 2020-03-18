python setup.py sdist
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install -i https://test.pypi.org/simple/ br-nome-gen --force