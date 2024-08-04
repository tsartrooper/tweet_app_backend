from db import db

class UserModel(db.Model):
    
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String)
    nsfw = db.Column(db.Boolean)
    tweets = db.relationship("TweetModel", back_populates = "user", lazy = "dynamic", cascade = "all, delete")   