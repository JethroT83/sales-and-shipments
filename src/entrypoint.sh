#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME="${PROJECT_NAME:-app}"    # change if you prefer another name
PROJECT_DIR="/app/${PROJECT_NAME}"

if [ ! -f "/app/manage.py" ] && [ ! -d "${PROJECT_DIR}" ]; then
  echo "Bootstrapping Django project '${PROJECT_NAME}'..."
  django-admin startproject "${PROJECT_NAME}" /app
fi

python manage.py migrate
exec "$@"