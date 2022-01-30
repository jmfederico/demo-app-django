#!/usr/bin/env bash
set -Eeuo pipefail

# Run migrations automatically the first time.
# After the first time, migrations should be run manually.
if PYTHONUNBUFFERED=0 python manage.py migrate --plan | grep --silent "contenttypes.0001_initial"
then
    python manage.py migrate
    python manage.py createcachetable
    python manage.py collectstatic --noinput
fi

exec "$@"
