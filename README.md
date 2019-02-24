# Neargreen V2

## Goal

Near Green is a web application that aims to make healthy food accessible to the city of Philadelphia.

## Features

- Single Page Application (SPA) where all requests are served by Django Rest Framework (DRF) and consumed by Vue.js

## Requirements

- Python 3.6
- pip
- virtualenv
- Yarn
- Vue Cli 3

## Installation

```bash
$ yarn install
$ virtualenv venv && source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

## Run Development Servers

```bash
$ python manage.py runserver
```

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
