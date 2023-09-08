from flask import Flask, json, jsonify, request
from flask_pymongo import PyMongo

from user_repository import UserRepository
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/corider"
mongo = PyMongo(app)
user_repository = UserRepository(mongo.db)


# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = user_repository.get_all_users()
    return json.dumps(users, default=str), 200, {'content-type': 'application/json'}


# Create user
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    user_id = user_repository.create_user(user_data)
    user = user_repository.get_user_by_id(user_id)
    return json.dumps(user, default=str), 201, {'content-type': 'application/json'}


# Get user by ID
@app.route('/users/<string:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_repository.get_user_by_id(ObjectId(user_id)) if ObjectId.is_valid(user_id) else None
    if user:
        return json.dumps(user, default=str), 200, {'content-type': 'application/json'}
    else:
        return json.dumps({"status": 404, "message": 'User Not Found'}), 404, {'content-type': 'application/json'}


# Update user by ID
@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_data = request.json
    result = user_repository.update_user(ObjectId(user_id), updated_data) if ObjectId.is_valid(user_id) else 0
    if result > 0:
        updated_user = user_repository.get_user_by_id(ObjectId(user_id))
        return json.dumps(updated_user, default=str), 200, {'content-type': 'application/json'}
    else:
        return json.dumps({"status": 404, "message": 'User not found'}), 404, {'content-type': 'application/json'}


# Delete user by ID
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = user_repository.delete_user(ObjectId(user_id)) if ObjectId.is_valid(user_id) else 0
    if result > 0:
        return json.dumps({"status": 204, "message": 'User Deleted'}), 204,
    else:
        return json.dumps({"status": 404, "message": 'User Not Found'}), 404, {'content-type': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True)
