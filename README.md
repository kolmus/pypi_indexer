# pypi_indexer

cron jobs: 

curl -o pypi_app/management/xml/packages.xml https://pypi.org/rss/packages.xml

python manage.py get_new_packages