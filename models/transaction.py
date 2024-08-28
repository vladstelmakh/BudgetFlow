# models/transaction.py
from database import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, amount, user_id):
        self.amount = amount
        self.user_id = user_id


