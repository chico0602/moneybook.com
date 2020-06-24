FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install django-bootstrap4
RUN pip install social-auth-app-django
RUN pip install -r requirements.txt
ADD . /code/