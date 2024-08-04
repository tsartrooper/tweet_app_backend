from flask import Flask
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256

from db import db
from models import UserModel
from schemas import PlainUserSchema


blp = Blueprint("user", __name__, description = "Operations on user.")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(PlainUserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.user_name == user_data["user_name"]).first():
            abort(
                409,
                message = "a user with that name already exists."
            )
        
        user = UserModel(
            user_name = user_data["user_name"],
            password = pbkdf2_sha256.hash(user_data["password"],)
        )
        db.session.add(user)
        db.session.commit()
        
        return {"message": "User created successfully."}, 201

@blp.route("/users")
class AllUsers(MethodView):
    @blp.response(200, PlainUserSchema(many=True))
    def get(self):
        return UserModel.query.all()