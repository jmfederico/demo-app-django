#!/usr/bin/env bash
set -Eeuo pipefail

# Run migrations automatically the first run.
# After the first time, migrations should be run manually.
if python manage.py migrate --plan | grep --silent "contenttypes.0001_initial"
then
    python manage.py migrate
fi

exec "$@"
