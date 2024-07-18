FROM python:3.11

WORKDIR /usr/src/app

COPY req.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r req.txt && \
    pip install celery

COPY . .

RUN python manage.py collectstatic --noinput && \
    python manage.py makemigrations

CMD celery -A config worker --loglevel=info

