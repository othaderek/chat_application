from .base import db
class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(13))

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"<User {self.name}>"