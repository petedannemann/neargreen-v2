# Instamap

## Goal

Create an Instagram clone that geotags each post and displays your posts on a map

## Features

- Single Page Application (SPA) where all requests are served by Django Rest Framework (DRF) and consumed by Vue.js

## Requirements

- Python 3.6
- Pipenv
- Yarn
- Vue Cli 3

## Installation

```bash
$ yarn install
$ pipenv install --dev & pipenv shell
$ python manage.py migrate
```

## Run Development Servers

```bash
$ pipenv run python manage.py runserver
```

```bash
$ yarn serve
```

## URL Routes

`/` Index, displays all posts

## API Routes

`/api/posts` Display all posts

`/api/post/<postid>` Display a specific post

`/api/register` Register a profile

`/api/auth/login` Login a user

`/api/auth/logout` Logout a user
