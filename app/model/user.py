from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    tel = db.Column(db.String)
    gender = db.Column(db.String)

    __tablename__ = 'tb_user'