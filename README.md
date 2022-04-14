
# Pokedex API

Pokedex API is a fully featured RESTful API that tracks your favorite Pokemons! To get started as fast as possible make sure you have the following requirements checked out:
- OS: Windows (WSL2) or Linux distro
 - Docker v20.10.12+
 - Docker Compose v2.2.3+

## Features

 - JWT Authentication
 - CRUD operations on pokemons (includes private and public lists)
 - Random number endpoint
 - Unit testing
 - Swagger Docs
 - Production environment using NGINX + Gunicorn.

## Installation

 1. Clone the repository on your local machine.

2. Select an environment and use the commands provided in that section, you can choose **Development** OR **Production**. To get up and running as soon as possible, use **Development**.

### Development

To spin up the containers:

    docker compose up -d

If this is your first time running the project, you will have to run migrations afterwards:

    docker compose exec web python manage.py migrate --noinput

At this point you can start interacting with the API, please view the swagger documentation on: http://localhost:8000/docs/

To run unit tests:

    docker compose exec web pytest

To stop all containers:

    docker compose stop
To remove all containers and their associated volumes:

    docker compose down -v



### Production
In case you want to run a production ready environment in your local system, create two files on the root of the project (where this README.md is located) with their corresponding values:

 1. **.env.prod**
 ```
  SECRET_KEY=django-insecure-%yt)i8)#&i@@pxn$!j$53#d)-c17u^)_8cy30%9vwy+9!s*j9b
  DEBUG=0
  DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
  SQL_ENGINE=django.db.backends.postgresql
  SQL_DATABASE=pokedex_db
  SQL_USER=ash
  SQL_PASSWORD=thisismypokedex
  SQL_HOST=db
  SQL_PORT=5432
  DATABASE=postgres
  ```
  2. **.env.prod.db**
  ```
	POSTGRES_DB=pokedex_db
	POSTGRES_USER=ash
	POSTGRES_PASSWORD=thisismypokedex
  ```

In case you want to use a different database name, user or password, remember that their values must be the same in each file, i.e. POSTGRES_DB = SQL_DATABASE. 

To spin up the containers:

    docker compose -f docker-compose.prod.yml up -d

If this is your first time running the project, you will have to run migrations afterwards:

    docker compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
At this point you can start interacting with the API, please view the swagger documentation on: http://localhost:1337/docs/

To run unit tests:

    docker compose -f docker-compose.prod.yml exec web pytest

To stop all containers:

    docker compose -f docker-compose.prod.yml stop
To remove all containers and their associated volumes:

    docker compose -f docker-compose.prod.yml down -v

