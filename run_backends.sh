#!/bin/sh

while ! nc -z db 5432; do
    echo "Waiting for PostgreSql to start..."
    sleep 1
done

while ! nc -z redis 6379; do
    echo "Waiting for Redis to start..."
    sleep 1
done


echo "$1"
cd /opt

if [ "$1" = "worker" ]; then
    echo "Run workers..."
    python ./manage.py runworker --threads 4
else
    echo "Migrate..."
    python ./manage.py migrate --noinput

    echo "Run server..."
    daphne s112.asgi:channel_layer -b 0.0.0.0
fi
