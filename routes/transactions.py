from flask import Blueprint, request, jsonify
from app import mongo  # Імплементація mongo для доступу до бази даних

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/add', methods=['POST'])
def add_transaction():
    data = request.json
    mongo.db.transactions.insert_one(data)  # Додаємо документ до колекції `transactions`
    return jsonify({"message": "Transaction added successfully"}), 201

@transactions_bp.route('/list', methods=['GET'])
def list_transactions():
    transactions = list(mongo.db.transactions.find())  # Отримуємо всі документи з колекції `transactions`
    return jsonify(transactions), 200









