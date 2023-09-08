from flask_pymongo import PyMongo


class UserRepository:
    def __init__(self, db):
        self._db = db

    def get_all_users(self):
        users_cursor = self._db.users.find()
        users = [user for user in users_cursor]
        return users

    def get_user_by_id(self, user_id):
        return self._db.users.find_one({"_id": user_id})

    def create_user(self, user_data):
        result = self._db.users.insert_one(user_data)
        return result.inserted_id

    def update_user(self, user_id, updated_data):
        update_result = self._db.users.update_one({"_id": user_id}, {"$set": updated_data})
        return update_result.modified_count

    def delete_user(self, user_id):
        delete_result = self._db.users.delete_one({"_id": user_id})
        return delete_result.deleted_count
