from datetime import datetime
import json
import os
from flask import Flask, jsonify, request, render_template_string, flash, redirect
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
from sqlalchemy.orm import aliased
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv, find_dotenv
import config
from models import *
from security import *
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
import pandas as pd

load_dotenv(find_dotenv())

app = Flask(__name__)
CORS(app)


app.config.from_object(config)
# print(app.config)

db.init_app(app)

# Migrations
migrate = Migrate(app, db)
ma.init_app(app)


jwt = JWTManager(app)


@app.route("/refresh", methods=["POST"])
@jwt_required()
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify({"access_token": access_token}), 200


@app.route("/add_role", methods=["POST"])
@jwt_required()
@check_roles(roles_required=["admin"])
def add_role():
    data = request.get_json()

    if not data or "name" not in data or "description" not in data:
        return jsonify({"message": "Invalid input data"}), 400

    name = data["name"]
    description = data["description"]

    existing_role = Role.query.filter_by(name=name).first()
    if existing_role:
        return jsonify({"message": "Role with the same name already exists"}), 400

    role = Role(name=name, description=description)
    db.session.add(role)
    db.session.commit()

    return jsonify({"message": "Role added successfully"}), 201


@app.route("/register", methods=["POST"])
@jwt_required()
@check_roles(roles_required=["admin"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid input data"}), 400

    email = data.get("email")
    password = data.get("password")
    role_names = data.get("roles", [])
    print(data)
    print(role_names)

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    # Create a new user and save it to the database
    user = User(email=email, password=hash_password(password))

    # Associate roles with the new user
    for role_name in role_names:
        role = Role.query.filter_by(name=role_name).first()
        if role:
            user.roles.append(role)

    db.session.add(user)
    db.session.commit()

    # Generate a JWT token for the new user
    access_token = create_access_token(identity=user.email)

    return jsonify({"access_token": access_token}), 201


@app.route("/delete_user", methods=["POST"])
@jwt_required()
@check_roles(roles_required=["admin"])
def delete_user():
    data = request.get_json()

    if not data or "email" not in data:
        return jsonify({"message": "Invalid input data"}), 400

    email_to_delete = data["email"]

    user_to_delete = User.query.filter_by(email=email_to_delete).first()

    if not user_to_delete:
        return jsonify({"message": "User to delete not found"}), 404

    # Remove the user's roles
    user_to_delete.roles.clear()

    # Delete the user
    db.session.delete(user_to_delete)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print(data)
    if data is not None and "email" in data and "password" in data:
        email = data["email"]
        password = data["password"]
        user = User.query.filter_by(email=email).first()

        if user:
            if verify_password(password, user.password):
                # response = jsonify({"msg": "login successful"})
                access_token = create_access_token(identity=email)
                # possbility: set_access_cookies(response, access_token)
                roles = [role.name for role in user.roles]
                response = jsonify({"access_token": access_token, "roles": roles})
                return response, 200

    return jsonify({"message": "Authentication failed"}), 401


@app.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    # Der Token ist noch gültig, man könnte logik implementieren, dass Token mit Datenbank abeglichen werden muss und dann hier gelöscht wird
    # Aber für unseren use-case reicht erstmal so
    print("logged out")
    return jsonify({"message": "Logged out sucessfully"}), 200


@app.route("/verify", methods=["POST"])
@jwt_required()
def verify():
    print(request.headers)
    return jsonify({"message": "Authentication successful"}), 200


@app.route("/")
@jwt_required()
@check_roles(roles_required=["admin"])
def home():
    return render_template_string("Hello")


if __name__ == "__main__":
    # Hier entsprechend ändern
    app.run(debug=True, host="0.0.0.0", port=8081)
    with app.app_context():
        create_super_user()
