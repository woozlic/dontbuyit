web: daphne dontbuyit.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker websocket --settings=dontbuyit.settings -v2