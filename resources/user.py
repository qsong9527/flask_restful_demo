from flask_restful import Resource


class User(Resource):

    def post(self, uid):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Create user."
        }
        return ret_val

    def delete(self, uid):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Delete user."
        }
        return ret_val

    def put(self, uid):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Update user."
        }
        return ret_val

    def get(self, uid):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Get user."
        }
        return ret_val


class Users(Resource):

    def get(self):
        ret_val = {
            "ret_code": "200",
            "ret_msg": "Search user."
        }
        return ret_val