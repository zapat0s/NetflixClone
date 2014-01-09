NetflixClone
============

A Netflix clone that allows users to browse and watch movies and TV shows.

NetflixClone consists of two parts currently. A Django based back end that
provides a REST API and an Angularjs based front end that consumes the REST API.

The hope is that the REST API exposed by the server will become powerful enough
to connect to a collection of apps.

Currently the only app is a simple Web based app also hosted by the server.

Dependencies
*   [Django](http://djangoproject.com)
*   [South (recommended)](http://south.aeracode.org/)
*   [django-rest-framework](http://django-rest-framework.org/)
*   [django-taggit](https://github.com/alex/django-taggit)
*   [django-sendfile](https://github.com/johnsensible/django-sendfile)

NetflixClone can be installed without South however it is recommended to help
with database migrations in future versions.


Installation
What follows is a full installation using Apache, PostgreSQL, and mod_wsgi. I
have found that this combination works very well. Please feel free to add
additional ways of setting up NetflixClone as you find them.

Step 1: Setup PostgreSQL

Step 2: Setup NetflixClone

Step 3: Setup Apache

