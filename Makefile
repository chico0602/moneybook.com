makemigrations:
    docker-compose run --rm web python3 manage.py makemigrations

migrate:
    docker-compose run --rm web python3 manage.py migrate

createsuperuser:
    docker-compose run --rm web python3 manage.py createsuperuser