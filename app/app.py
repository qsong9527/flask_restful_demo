from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

from app.routes.user import User, Users

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'User Micro-service',
    'version': '1.0.0'
}
swagger = Swagger(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/db_user"
db = SQLAlchemy(app)

api = Api(app)

api.add_resource(User, '/api/v1/user/<uid>')
api.add_resource(Users, '/api/v1/users')

@app.route("/")
def index():
    return "Hello Flask"
