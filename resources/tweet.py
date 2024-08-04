from flask import Flask
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError


from db import db
from models import UserModel, TweetModel
from schemas import TweetSchema

blp = Blueprint("tag", __name__, description = "Users tweets.")

@blp.route("/user/<string:user_id>/tweets")
class TweetOfUser(MethodView):
    @blp.response(200, TweetSchema(many = True))
    def get(self, user_id):
        return TweetModel.query.filter(TweetModel.user_id == user_id).all()