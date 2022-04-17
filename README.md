
# Pokedex API

Pokedex API is a fully featured RESTful API that tracks your favorite Pokemons!  

A live version is up and running here: http://ec2-34-224-27-53.compute-1.amazonaws.com/docs/

If you want to run it on your machine, keep reading.


## Requirements

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

## Installation

 1. Clone the repository on your local machine.
 2. Spin up the containers for only **ONE** of the following environments:

    **Important note**: In case you have launched the development containers and want to switch to production or vise versa, remove all containers with their respective volumes and images, and then run the containers for the other environment.


### For Development

**To spin up the containers:**

    docker compose up -d

At this point you can start interacting with the API, please view the swagger documentation on: http://localhost:8000/docs/

**To run unit tests:**

    docker compose exec web pytest

**To stop all containers:**

    docker compose stop

**To remove all containers with their associated volumes and images:**

    docker compose down -v --rmi all



### For Production

**To spin up the containers:**

    docker compose -f docker-compose.prod.yml up -d

At this point you can start interacting with the API, please view the swagger documentation on: http://localhost:1337/docs/

**To run unit tests:**

    docker compose -f docker-compose.prod.yml exec web pytest

**To stop all containers:**

    docker compose -f docker-compose.prod.yml stop

**To remove all containers with their associated volumes and images:**

    docker compose -f docker-compose.prod.yml down -v --rmi all


