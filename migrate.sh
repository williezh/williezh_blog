python manage.py collectstatic
python mysql_conf_swift.py default_to_slave
python manage.py dumpdata > sqlite3_data.json
python mysql_conf_swift.py
python createdatabase.py
python manage.py migrate
python manage.py loaddata sqlite3_data.json
