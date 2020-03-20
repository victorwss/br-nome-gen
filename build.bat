pip install -r requirements.txt
pip install ./ --upgrade
mypy --disallow-untyped-defs --disallow-untyped-calls --disallow-incomplete-defs --check-untyped-defs --disallow-untyped-decorators --strict --show-traceback br_nome_gen/__init__.py br_nome_gen/br_nome_gen.py tests/teste.py
python tests/teste.py 100