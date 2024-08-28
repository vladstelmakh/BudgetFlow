from flask import Blueprint, request, jsonify
from app import mongo  # Імплементація mongo для доступу до бази даних

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    # Ваш код для реєстрації користувача
    return jsonify({"message": "User registered successfully"}), 201














