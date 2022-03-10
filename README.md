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

1. api/auth/users/ - Used for registration -POST
2. api/auth/jwt/create/ - Used for Signin and returns JWT tokens -POST
3. /api/video/ - Used to get all Movies -GET
4. /api/profile/ - Used to get Profiles -GET
5. /api/profile/create/ -Used to create profiles using the uuid -POST
6. /api/watch/str:pk/ -Used to get movies based on the profile rating and uuid -GET
7. /api/movie/detail/str:movie_id/ -Used to get movie details using the movies uuid -GET
8. /api/movie/play/str:movie_id/ - Used to get videos url using the videos uuid

-Get more Authentication Endpoints from [djoser](https://djoser.readthedocs.io/en/latest/base_endpoints.html)


## Authors

-[Leslie Shumba](https://github.com/layan2k)
-[Richard Osei](https://github.com/mrbridge-mrbridge)
-[Nmesoma Solomon Peter](https://github.com/Nmesoma-solomon-peter)