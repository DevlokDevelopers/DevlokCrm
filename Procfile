web: uvicorn devlok_crm.asgi:application --host 0.0.0.0 --port 8000 --workers 2
worker: celery -A devlok_crm worker --loglevel=info
