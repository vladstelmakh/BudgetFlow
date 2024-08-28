from flask import Flask
from flask_pymongo import PyMongo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # Завантажуємо конфігурацію з Config класу

mongo = PyMongo(app)  # Ініціалізуємо PyMongo з Flask-додатком

# Імпортуємо маршрути після ініціалізації додатку
from routes.auth import auth_bp
from routes.transactions import transactions_bp

app.register_blueprint(auth_bp)
app.register_blueprint(transactions_bp)

@app.route('/')
def index():
    return "Welcome to the Finance Manager!"












