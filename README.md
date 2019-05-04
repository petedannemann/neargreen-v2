# Neargreen V2

## Goal

Near Green is a web application that aims to make healthy food accessible to the city of Philadelphia.

## Features

- Single Page Application (SPA) where all requests are served by Django Rest Framework (DRF) and consumed by Vue.js

## Backend Requirements

- Docker
- docker-compose

## Frontend Requirements

- Yarn
- Vue Cli 3

## Run Backend Development Server

```bash
$ docker-compose -f docker-compose.dev.yml build
$ docker-compose -f docker-compose.dev.yml up
```

## Run Frontend Development Server

```bash
$ yarn serve
```

## Run Backend Production Server

```bash
$ docker-compose -f docker-compose.prod.yml build
# The first time, seed the database, after that don't include that env var
$ SEED_DB=true docker-compose -f docker-compose.prod.yml up
```

## URL Routes

`/` Index, displays all stores

## API Routes

`/api/stores` Display all stores

`/api/stores/<storeid>` Display a specific store

`/api/register` Register a profile

`/api/auth/login` Login a user

`/api/auth/logout` Logout a user
