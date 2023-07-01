# Cookbook-flaskpocket

A cookbook API built on top of Pocketbase wrapped in Flask to provide a logic layer.

The goal is to create a lightweight, clean, and straightforward cookbook that's easy to input recipes and easy to share recipes.

# Installation

```
# TODO: update this when Flask comes into play
cp .env.example .env
vim .env
docker compose up
```

# Development

There's a `Makefile` helper tool in the `/dev` folder that runs `curl` commands for you so you don't need a UI interface to work with this API.  Check the README in that folder for more details. 

# Technical justification

Pocketbase already provides most of the repetitive setup work involved with Django/DRF, such as setting up an authentication system and exposing API endpoints.  Instead of create a heavy DRF API, I decided just to "make do" with whatever I could manipulate Pocketbase to do.

The entire Pocketbase instance is wrapped by Flask which (at the moment) does simple things like favoriting recipes.  Eventually, this logic layer can be used to perform automation like extracting ingredients from a recipe or hooking up to third-party providers (like S3 buckets and DALLE).