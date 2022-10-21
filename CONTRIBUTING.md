# Instructions to install all dependencies
```
python -m pip install --upgrade pip
python -m pip install virtualenv
python -m venv .venvide
.\.venvide\Scripts\activate
python -m pip install pip-tools
pip-compile requirements.in
pip-compile requirements-dev.in
```
=> install for prod:
```
pip-sync requirements.txt
```
=> install for dev:
```
pip-sync requirements.txt requirements-dev.txt
```

To apply, in prod envirronment, tox with task for:
- black   
- typing
- flake 
- lint 
- test_unit