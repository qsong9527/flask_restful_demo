from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from resources.user import User, Users

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'User Micro-service',
    'version': '1.0.0'
}
swagger = Swagger(app)

api = Api(app)

api.add_resource(User, '/api/v1/user/<uid>')
api.add_resource(Users, '/api/v1/users')

@app.route("/")
def index():
    return "Hello Flask"
