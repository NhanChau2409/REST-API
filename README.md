# REST API 

It is a simple API web with Python for ogarnizing employee salary 

**Description**:

Using a small database to store data about employee - name, salary. Then arrange data with JSON string.

**Operations**:
- add new data
- delete data
- query all data
- query single data by id
- update data by id

**Database**:
- SQLite

**Library**:
- Flask
    - web framework for Python
    - It is light, simple, and well document

-  Flask-SQLAlchemy
    - thin integration layer for Flask and SQLAlchemy
    - SQLAlchemy is a Object-relational Mappers (ORMS) library
    - It's purpose is connect and perform query from database

- Flask-Marmallow
    - thin integration layer for Flask and Marshmallow
    - Marshmallow is object serializing, desrializing libraries
    - It's purpose is serializing object to JSON response for requests

- Marshmallow-SQLAlchemy
    - thin integration for Marshmallow-SQLAlchemy
    - It's purpose is integrating those 2 libraries

## Installation

**Environment**:
- Visual Studio Code
- Python 3.5.10

**Steps**:
- download pipenv package interminal

    `pip3 install pipenv`
- access to virtual environment

    `pipenv shell`

- download all neccessary package for project

    `pipenv --dev`

## References

[**Flask**]("https://flask.palletsprojects.com/en/2.2.x/quickstart/")

[**Flask-Marshamllow**]("https://flask-marshmallow.readthedocs.io/en/stable/")

[**Flask-SQLAlchemy**]("https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/")