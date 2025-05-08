web: gunicorn devlok_crm.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
worker: celery -A devlok_crm worker --loglevel=info
