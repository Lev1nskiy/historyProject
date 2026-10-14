#!/usr/bin/env bash
# Запуск приложения: готовит виртуальное окружение и поднимает Flask.
#
#   ./run.sh            # http://0.0.0.0:5000
#   PORT=8000 ./run.sh  # другой порт
#   FLASK_DEBUG=0 ./run.sh
set -euo pipefail

cd "$(dirname "$0")"

VENV="${VENV:-.venv}"
PYTHON="${PYTHON:-python3}"

if [ ! -x "$VENV/bin/python" ]; then
    echo "==> создаю виртуальное окружение в $VENV"
    "$PYTHON" -m venv "$VENV"
    "$VENV/bin/pip" install --quiet --upgrade pip
    if [ -f requirements.txt ]; then
        echo "==> устанавливаю зависимости из requirements.txt"
        "$VENV/bin/pip" install --quiet -r requirements.txt
    fi
fi

echo "==> запускаю сервер на ${HOST:-0.0.0.0}:${PORT:-5000}"
exec "$VENV/bin/python" app.py
