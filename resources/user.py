from bson import ObjectId
from flask import json, jsonify
from flask import request

from flask_restful import Resource, abort


def get_user_data(user_data):
    if user_data['_id']:
        user_data['_id'] = str(user_data['_id'])
    return user_data


class Users(Resource):

    def __init__(self, **kwargs):
        self._user_repository = kwargs['user_repository']

    def get(self):
        users = self._user_repository.get_all_users()
        return [get_user_data(user) for user in users]

    def post(self):
        user_data = request.json
        user_id = self._user_repository.create_user(user_data)
        user = self._user_repository.get_user_by_id(user_id)
        return get_user_data(user), 201


class User(Resource):

    def __init__(self, **kwargs):
        self._user_repository = kwargs['user_repository']

    def get(self, user_id):
        user = self._user_repository.get_user_by_id(ObjectId(user_id)) if ObjectId.is_valid(user_id) else None
        if user:
            return get_user_data(user)
        else:
            return abort(404, status=404, message="User Not Found")

    def delete(self, user_id):
        user = self._user_repository.delete_user(ObjectId(user_id)) if ObjectId.is_valid(user_id) else 0
        if user > 0:
            return '', 204
        else:
            return abort(404, status=404, message="User Not Found")

    def put(self, user_id):

        if not ObjectId.is_valid(user_id):
            return abort(404, status=404, message="User Not Found")

        _id = ObjectId(user_id)
        if not self._user_repository.get_user_by_id(_id):
            return abort(404, status=404, message="User Not Found")

        user_data = request.json
        user_data["_id"] = _id
        self._user_repository.update_user(_id, user_data)
        return get_user_data(user_data)
