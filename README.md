# NOTE: This is a test task
## Overview
VehicleDriverAPI is the simple API was written in Python and
[Django REST framework](https://www.django-rest-framework.org/).
It is an example of implementation of REST API for a fleet of vehicles 
with drivers.
## Setup
Visit [SETUP.md](./SETUP.md) for installation and getting started
## [Usage](./SETUP.md#Available Routes)
[Here](./SETUP.md#Available Routes) you can find out usage of requests.
You can use [Postman](https://www.postman.com/) for using APIs or debug mode(default).
## JSON Schemas
The driver:
```
{
    "type": "object",
    "title": "The Driver schema",
    "properties": {
        "id": {
            "type": "integer",
            "examples": 3
        },
        "first_name": {
            "type": "string",
            "examples": "Jhon",
            "pattern": "^[a-zA-Z]*$"
        },
        "last_name": {
            "type": "string",
            "examples": "Doe",
            "pattern": "^[a-zA-Z]*$"
        },
        "created_at": {
            "type": "string",
            "format": "date-time",
            "examples": "09/12/2021 15:06:15"
        },
        "updated_at": {
            "type": "string",
            "format": "date-time",    
            "examples": "10/12/2021 18:00:25"
        },
    },
}
```
The vehicle:
```
{
    "type": "object",
    "title": "The Vehicle schema",
    "properties": {
        "id": {
            "type": "integer",
            "examples": 3
        },
        "make": {
            "type": "string",
            "examples": "Germany, VAG"
        },
        "model": {
            "type": "string",
            "examples": "Golf 5"
        },
        "plate_number": {
            "type": "string",
            "examples": "AA 5555 BB",
            "pattern": "\b[A-Z]{2}\s[0-9]{4}\s[A-Z]{2}\b"
        },
        "created_at": {
            "type": "string",
            "format": "date-time",
            "examples": "09/12/2021 15:06:15"
        },
        "updated_at": {
            "type": "string",
            "format": "date-time",    
            "examples": "10/12/2021 18:00:25"
        },
        "driver_id": {
            "default": "null",
            "type": "integer",    
            "examples": [3, null],
            "description": "FK to Driver, OneToOne relationship"
        }
    },
}
```
