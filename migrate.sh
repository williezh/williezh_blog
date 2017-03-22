python manage.py collectstatic
python mysql_conf_swift.py default_to_slave
python manage.py dumpdata > data_mysql.json
python mysql_conf_swift.py
python createdatabase.py
python manage.py migrate
python manage.py createsuperuser --username willie --email jaket5219999@126.com
python manage.py loaddata data_mysql.json
