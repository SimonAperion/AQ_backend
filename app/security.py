from flask import current_app
import hashlib
from models import *
from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity

def check_roles(roles_required):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            # Get the current user's email from the JWT token
            current_user_email = get_jwt_identity()
            

            # Fetch the user from the database using the email
            user = User.query.filter_by(email=current_user_email).first()

            if not user:
                return jsonify({'message': 'User not found'}), 404

            user_role_names = {role.name for role in user.roles} if user.roles else set()
            required_role_names = set(roles_required)
            print(user_role_names)
            # Check if the user has the required role names
            if not required_role_names.issubset(user_role_names):
                return jsonify({'message': 'Insufficient roles'}), 403

            return func(*args, **kwargs)

        return decorated_function

    return decorator



def hash_password(password):
    salt = current_app.config['SECURITY_PASSWORD_SALT']
    password = password.encode()
    salt= salt.encode()
    key = hashlib.pbkdf2_hmac(hash_name='sha256',password=password,salt=salt, iterations=100000,dklen=64)
    return key.hex()

def verify_password(password, hashed_password):
    new_hashed = hash_password(password)
    if new_hashed == hashed_password:
        return True
    else:
        return False
    
    