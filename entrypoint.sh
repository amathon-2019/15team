#!/bin/bash

set -e

# Run
case "$1" in
    start)
        echo "Building static assets"  
        npm run build
        echo "Apply database migrations"  
        python3 manage.py makemigrations
        python3 manage.py migrate
        python3 manage.py runserver 0.0.0.0:8765
esac
