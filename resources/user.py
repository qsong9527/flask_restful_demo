from flask_restful import Resource
from flasgger import swag_from

class User(Resource):

    @swag_from('../apidocs/user_create.yml')
    def post(self, uid):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Create user."
        }
        return ret_val

    @swag_from('../apidocs/user_delete.yml')
    def delete(self, uid):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Delete user."
        }
        return ret_val

    @swag_from('../apidocs/user_update.yml')
    def put(self, uid):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Update user."
        }
        return ret_val

    @swag_from('../apidocs/user_get.yml')
    def get(self, uid):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Get user."
        }
        return ret_val


class Users(Resource):

    @swag_from('../apidocs/user_search.yml')
    def get(self):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Search user."
        }
        return ret_val