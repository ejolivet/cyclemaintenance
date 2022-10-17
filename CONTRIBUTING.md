# Instructions to install all dependencies
```
python -m pip install virtualenv
python -m venv .venv
.\.venv\Scripts\activate
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
