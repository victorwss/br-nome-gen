python setup.py sdist
python -m twine upload dist/*
pip install -i https://pypi.org/simple/ br-nome-gen --force