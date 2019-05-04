# Neargreen V2

## Goal

Near Green is a web application that aims to make healthy food accessible to the city of Philadelphia.

## Features

- Single Page Application (SPA) where all requests are served by Django Rest Framework (DRF) and consumed by Vue.js

## Backend Requirements (w/o Docker)

- Python 3.6
- pip
- virtualenv

## Backend Requirements (w/ Docker)

- Docker
- docker-compose

## Frontend Requirements

- Yarn
- Vue Cli 3

## Backend Installation (w/o Docker)

```bash
$ yarn install
$ virtualenv venv && source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

## Run Backend Development Server (w/o Docker)

```bash
$ python manage.py runserver
```

## Run Backend Development Server (w/ Docker)

```bash
$ docker-compose build
# The first time, seed the database, after that don't include that env var
$ SEED_DB=true docker-compose up
```

## Run Frontend Development Server

```bash
$ yarn serve
```

## URL Routes

`/` Index, displays all stores

## API Routes

`/api/stores` Display all stores

`/api/stores/<storeid>` Display a specific store

`/api/register` Register a profile

`/api/auth/login` Login a user

`/api/auth/logout` Logout a user
