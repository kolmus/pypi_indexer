echo "This script will migrate db and add first packages to db"
echo "It will also install cron and add crontab job - geting new packages"
read -n1 -r -p "Press any key to continue"
python manage.py migrate
python manage.py restore_db

apt-get update
apt-get -y install cron

crontab -l | { cat; echo "55 23 * * * bash /usr/app/get_packages.sh"; } | crontab -
echo "crontab:"
crontab -l
cron
