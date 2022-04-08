# PYPI_indexer
## 1. Description
Simple Program for indexing changes in packages on PyPi
## 2. TECH
Python3.8,
PostgreSQL
Django,
Django REST,
Django Arhive,
Requests,
Xmltodict
BeautifullSoup
Pytest,
Docker,
Docker-compose,
Bootstrap tempate (HTML + CSS),
Faker (exemples in tests),

## 3. Installation
### System requirements:
1. Docker
2. Docker-compose
3. Internet connection
### Commands:
`docker-compose build` - builds container

`docker-compose up -d` - runs all 2 conteiners:
1. `pypi_db` =  official image with postgresql
2. `pypi_` = container with PYPI_indexer

### First Run:
1. `docker-compose up -d` - runs all 2 conteiners
2. `docker-compose run pypi bash ./install.sh` script migrates model of package to database, restores first packages from archive and set cronjob for updating averyday at 23:55
## 4. Variabes to set
To set up in `settings.py`:

* `ARCHIVE_DIRECTORY` path to folder to store arhive tar packages
* `ADMIN_ENABLED` admin site - usles in this project but saved posibility for the future
* `TEST_ITEMS` number of fake packages to unit test for views
* `PACKAGES_PER_PAGE` number of packages on page - for paginator

To set in `.env`:
* `SECRET_KEY` exemple: django-insecure-&f76(gy#b#+hsi6yc#(hy-j)y@lc-!8!m4zomn4x3vi!u2y&=h
* `DEBUG` e.g False
* `DJANGO_ALLOWED_HOSTS` = localhost 127.0.0.1 [::1]
* `DB_HOST` = pypi_doc_db
* `DB_NAME` = name of database which will be creategd in pypi_db container
* `DB_USER` = username in database
* `DB_PASSWORD`= password in database


## 5. Available scripts
* `docker-compose run pypi bash ./get_packages.sh` makes new archive and download newes Packages
* `docker-compose run pypi python manage.py get_new_packages` download newest packages without making archive file => **NOT RECOMENDED**
* `docker-compose run pypi python manage.py restore_db` restores db with **last** archive package => restorest old data or create again if its lost

## 6. PATHS
main page path `'/'` or localhost

API available on `/api/` method POST only, requires data: `{'search': x}` where x is word or words separated with 1 space ' ' and *not null*


### Unit tests
`docker-compose run pypi pytest`


