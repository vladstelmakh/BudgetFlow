from flask import Blueprint, request, jsonify
from db import db  # Імпортуємо `db` з db.py

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/create', methods=['POST'])
def create_transaction():
    data = request.json
    # Логіка створення транзакції
    return jsonify({"message": "Transaction created successfully"}), 201

