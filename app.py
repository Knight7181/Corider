from flask import Flask, json, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Api

from resources.user import Users, User
from user_repository import UserRepository
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/corider"
mongo = PyMongo(app)
user_repository = UserRepository(mongo.db)
api = Api(app)

api.add_resource(Users, '/users', resource_class_kwargs={'user_repository': user_repository})
api.add_resource(User, '/users/<string:user_id>', resource_class_kwargs={'user_repository': user_repository})


if __name__ == "__main__":
    app.run(debug=True)
