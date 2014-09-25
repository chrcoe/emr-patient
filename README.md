Fall 2014 Practicum
===================

# Electronic Medical Record System

* Python 2.7.x
* Django 1.7
* psycopg2 2.5.4 (postgresql connector) [Windows download page](http://www.stickpeople.com/projects/python/win-psycopg/ "psycopg2-windows")

The production server uses PostgreSQL so you will also need the Python library called psycopg2

If you are on Windows, make sure you download the compiled packages for your architecture as well as verifying the Python version it is for.

Example:

* psycopg2 v2.5.4, you have 64bit Windows and we are using Python 2.7... make sure to download the file named: psycopg2-2.5.4.win-amd64-py2.7-pg9.3.5-release.exe

I use linux, so the only suggestion I can offer is don't try to build anything from source if you are on Windows, it is much more hassle than it is worth.  There is almost always a precompiled binary for your version of Python and Windows arch.

_NOTE_: You can use the built in sqlite3 DB in your local_settings.py file (see the one included for an example) instead of installing and setting up PostgreSQL on your local dev machine.  If you do not intend to use PostgreSQL on your local machine, then you do not need the psycopg2 module.

To get started with Django, you can use:

https://docs.djangoproject.com/en/1.7/intro/tutorial01/

I have already created the base app in this repository, so we do not need to worry about that since we are all using the same app.
I would suggest you run through the tutorial from start to finish on your local machine separated from this repository so you have a grasp on how things work.

To create an admin user:

    ./manage.py createsuperuser --username=joe --email=joe@example.com

It will then ask for a password twice.  This superuser would only be created on your development server.

I will create super user accounts on the production server for everyone with a default password once it is up and running

You will be able to use the built in Django webserver to test the app locally before pushing it to the repository.

    ./manage.py runserver


For our project, you will most likely be working inside the emrapp folder.  All other folders/files are the config files I use on my production server just so I can keep them together.  Feel free to check them out and ask any questions, but please do not change them!

unfuddle commit message association/auto resolving tickets etc:
[link](http://unfuddle.com/support/docs/topics/powerful_commit_messages "powerful commit messages")


Version History
===============
_versioning based on [Semantic Versioning 2.0.0](http://semver.org/ "Semantic Versioning 2.0.0")_

#### current develop
* added develop branch

#### v0.0.1
* added base project
