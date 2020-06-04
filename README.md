# User Vehicles

Authenticated api to the vehicles belonging to a user

### How to run the app

- running the `docker-compose build` command will build all of the services needed
- running the `docker-compose up` script will launch the api at `localhost:80`
- run `pip3 install -r app/requirements.txt` will build test dependencies
- run tests with `py.test`

### Structure

The repository follows simplified version of a clean architecture structure with repositories, models and use_cases. The use_cases have not been places into classes and instead methods have been defined that are collected in one file.

see more at: https://www.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/

### Repositories

Each table in the `postgres` database is exposed by an interface on which sql will be ran. These can be found in the `app/sample/repositories` directory. In actual fact the interfaces are not entirely binded to the specific table as it depends on the sql that has been hardcoded due to some time constraints. Ideally they would have originated from a constant that was defined and used only in this repository.

### entities

Every object used in the project has been created in the `app/sample/entities` directory

### authentication

The project uses Oauth authentication. The `/token` endpoint expects Basic Auth headers to generate an encoded JWT bearer token from a username and a `SECRET` key once the username and password have been authenticated.

This bearer token is decoded and validated on further requests made to the api and the requests are scoped to the user that is encoded in the JWT.

To further authenticate I could have also hashed the passwords at the database level but encrypting fields in the import csv files seemed to be out of the scope of this task.

### database

The project uses a postgres relational database to represent the relational nature of the input data. A `db` service has been added on docker-compose, which runs the init files found in `app/db/postgres` to create the tables and populate the database with the csv data.
