# Introduction

The goal of this project is to provide minimalistic django project template that everyone can use, which _just works_ out of the box and has the basic setup you can expand on.


### Main features

*Rest API for a Netfix Like Page

* Separated dev and production settings


* User registration and logging in as demo

* Procfile for easy deployments

* Separated requirements files

* SQLite by default if no env variable is set


#  Fireside API

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/layan2k/fireside_back.git
    $ cd fireside_back

Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements.txt


Then simply apply the migrations:

    $ python manage.py migrate


You can now run the development server:

    $ python manage.py runserver

API main Endpoints

1. api/auth/users/ - Used for registration
2. api/auth/jwt/create/ - Used for Signin and returns JWT tokens