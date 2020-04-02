from flask import Flask
from flask_restful import Api

from resources.user import User, Users

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/user/<uid>')
api.add_resource(Users, '/users')

@app.route("/")
def index():
    return "Hello Flask"
