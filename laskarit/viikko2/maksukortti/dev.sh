#!/bin/sh
[ x$1 = x ] && echo "\
Pieni ja kevyt skripti helppoa kehitystyökalujen ajoa varten.

Käyttö: $0 <komento>

Komennot:

install    Asenna devausymäristö
pytest     Aja yksikkötestit pytestillä
pylint     Tarkista muotoilu pylintillä
covhtml    Tee haarakattavuus raportti html muodossa
covxml     Sama mutta xml muoto (codecov tarvitsee tämän)
covff      Tee html haarakattavuusraportti ja avaa se firefoxissa
all        Sama kuin '$0 covff && $0 pylint'
" && exit 0

[ $1 = install ] \
	&& PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring \
	   poetry install --no-root \
	&& exit 0

[ $1 = pytest ] \
	&& poetry run pytest -v \
	&& exit 0

[ $1 = pylint ] \
	&& poetry run python3 -m pylint src/maksukortti/ \
	&& exit 0

[ $1 = covhtml ] \
	&& poetry run python3 -m coverage run --branch -m pytest -v \
	&& poetry run python3 -m coverage html \
	&& exit 0

[ $1 = covxml ] \
	&& poetry run python3 -m coverage run --branch -m pytest -v \
	&& poetry run python3 -m coverage xml \
	&& exit 0

[ $1 = covff ] \
	&& poetry run python3 -m coverage run --branch -m pytest -v \
	&& poetry run python3 -m coverage html \
	&& firefox htmlcov/index.html \

[ $1 = all ] && poetry run python3 -m coverage run --branch -m pytest -v \
	&& poetry run python3 -m coverage html \
	&& firefox htmlcov/index.html \
	&& poetry run python3 -m pylint src/maksukortti/
