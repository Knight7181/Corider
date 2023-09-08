# Corider Assessment
This GitHub repository contains a Python Flask application that serves as a basic User Management API. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on user data stored in a MongoDB database. It provides endpoints to get all users, create a new user, retrieve a user by ID, update a user's information, and delete a user by their ID.

## Key Features:

### Flask Web Framework:
The application is built using Flask, a popular Python web framework, making it lightweight and easy to use.

### MongoDB Integration:
It uses Flask-PyMongo to connect to a MongoDB database. User data is stored in a database named "corider."

### User Repository: 
The code includes a user repository module (user_repository.py) that abstracts the interaction with the MongoDB database, providing functions for database operations.

### API Endpoints:
#### GET /users:
Retrieve a list of all users.
#### POST /users:
Create a new user and return their details.
#### GET /users/{user_id}:
Retrieve user details by specifying their unique ID.
#### PUT /users/{user_id}:
Update an existing user's information by specifying their ID.
#### DELETE /users/{user_id}:
Delete a user by their ID.

### Error Handling:
The API includes error handling for cases where a user is not found (HTTP 404) or when an invalid user ID is provided.

### JSON Responses:
All responses from the API are in JSON format, making it easy to integrate with other applications.
