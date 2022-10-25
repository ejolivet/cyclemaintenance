FROM python:3.10-slim-buster

# RUN apt install gcc libpq (no longer needed bc we use psycopg2-binary)

COPY requirements.txt /tmp/
COPY requirements-dev.txt /tmp/
RUN pip install pip-tools
RUN pip-sync /tmp/requirements.txt /tmp/requirements-dev.txt

RUN mkdir -p /app
COPY app/ /app/
RUN pip install -e /app
COPY tests/ /tests/
COPY db.sqlite3 /db.sqlite3

WORKDIR /app
ENV DJANGO_SETTINGS_MODULE=djangoproject.django_project.settings
CMD python /app/djangoproject/manage.py migrate && \
    python /app/djangoproject/manage.py runserver 0.0.0.0:80