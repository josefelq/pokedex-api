
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

### For Development

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



### For Production

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

