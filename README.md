# Flask CRUD API Builder

## Overview
This utility helps you to quickly generate boiler-plate code for a sample CRUD Rest API.

You can view a live demo at: [crudapibuilder.herokuapp.com](https://crudapibuilder.herokuapp.com/)

## Usage
 - Provide entity name. It could be anything like `users`, `groups`, etc. This becomes the base for all API endpoints.
 - Define the fields of entity in structure. Structure is defined as a key-value pair of field names and its data types (Pythonic).
   
   Sample sturcture:
   ```python
   {
       "name": str,
       "email": str,
       "username": str,
       "number": int,
   }
   ```
 - Click on `Build`. It will download a file called `boilerplate.py` which can be simply deployed with:
   ```python
   flask run
   ```
   - Pre-requisite:

     `$ pip install flask`

## API's Supported
 - **L**ist: `GET /<entity>`
 - **C**reate: `POST /<entity>`
 - **R**etrieve: `GET /<entity>/<id>`
 - **U**pdate: `PUT /<entity>/<id>`
 - **D**elete: `DELETE /<entity>/<id>`

## Phase-1 Deliverables
 - [x] Ability to define custom structure with different data types.
 - [x] Persistent storage using `JSON`.
 - [ ] Design with Bootstrap.
 - [ ] Ability to define required and optional attributes.

## Phase-2 Deliverables
 - [ ] Persistent storage using database.
 - [ ] Ability to define complex relationships between attributes.
 - [ ] Ability to define data constraints like: `unique`, `min-length`, `max-length`, etc.
 - [ ] Deploy an instance of `boilerplate.py` on the fly.
