#!/usr/bin/env bash
echo "Waiting for MySQL..."

while ! nc -z db 3306; do
  sleep 0.5
done

echo "MySQL started"

FLASK_APP=run.py flask db init
FLASK_APP=run.py flask db migrate
FLASK_APP=run.py flask db upgrade

cd /www
python run.py