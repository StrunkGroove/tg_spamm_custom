FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py makemigrations tg_accounts
RUN python manage.py makemigrations accounts
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput