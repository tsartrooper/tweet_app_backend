from db import db

class TweetModel(db.Model):
    
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(1000), unique = False, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique = False, nullable = False)
    user = db.relationship("UserModel", back_populates = "tweets", cascade = "all, delete")