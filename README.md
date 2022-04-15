
# Pokedex API

Pokedex API is a fully featured RESTful API that tracks your favorite Pokemons! To get started as fast as possible make sure you have the following requirements checked out:
- OS: Windows (WSL2) or Linux distro
 - Docker v20.10.12+
 - Docker Compose v2.2.3+

## Features

 - JWT Authentication
 - CRUD operations on pokemons (includes private and public lists). 
 - Random number endpoint
 - Unit testing
 - Swagger Docs
 - Production environment using NGINX + Gunicorn.

## Notes
- For **POST**, **PUT**, **PATCH** methods a Bearer Token is required: register then login and add the access_token provided to authorization header.
- Valid types for pokemon can be seen here: https://pokemon.fandom.com/wiki/Types. All uppercase. 

## Installation

 1. Clone the repository on your local machine.

**IMPORTANT**: You can only use **ONE** environment. In case you have launched the development containers and want to switch to production or vise versa, remove all containers and their volumes and then follow the steps provided for the other environment.

### For Development

To spin up the containers:

    docker compose up -d

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

At this point you can start interacting with the API, please view the swagger documentation on: http://localhost:1337/docs/

To run unit tests:

    docker compose -f docker-compose.prod.yml exec web pytest

To stop all containers:

    docker compose -f docker-compose.prod.yml stop

To remove all containers and their associated volumes:

    docker compose -f docker-compose.prod.yml down -v

