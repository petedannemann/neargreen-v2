#!/usr/bin/env bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    # Give the database time to initialize
    sleep 10
    echo "PostgreSQL started"
fi

if [ -n "$SEED_DB" ]; then
  python3 manage.py flush --no-input
  python3 manage.py migrate
fi

exec "$@"
