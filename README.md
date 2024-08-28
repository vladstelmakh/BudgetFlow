BudgetFlow is a financial management web application built with Flask and MongoDB. It allows users to manage their transactions and maintain a budget effectively.

Table of Contents
Features
Installation
Usage
Configuration
API Endpoints
License
Contributing
Features
User Registration: Users can register with a username and password.
Add Transactions: Users can add new transactions with details such as amount, category, and date.
View Transactions: Users can view a list of their transactions.
MongoDB Integration: Data is stored and managed using MongoDB.
Installation
To get started with BudgetFlow, follow these steps:

Clone the Repository:

bash
git clone https://github.com/vladstelmakh/budgetflow.git
cd budgetflow
Create and Activate a Virtual Environment:

bash
python -m venv venv
On Windows:

bash
venv\Scripts\activate
On macOS/Linux:

bash
source venv/bin/activate
Install Dependencies:

bash
pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the root directory and add the following configuration:

env
FLASK_ENV=development
SECRET_KEY=your_secret_key
MONGO_URI=mongodb+srv://username:password@cluster0.mongodb.net/your_database?retryWrites=true&w=majority
Run the Application:

bash
flask run
Navigate to http://localhost:5000 in your browser to view the application.

Usage
After setting up the project, you can start using BudgetFlow:

Add Transactions: Send a POST request to /add with the transaction details.
View Transactions: Send a GET request to /list with the user ID as a query parameter.
Configuration
Configuring MongoDB: Update the MONGO_URI in the .env file with your MongoDB connection string.
Secret Key: Update SECRET_KEY in the .env file with a secure key for session management.
API Endpoints
POST /add: Add a new transaction.

Request Body:
json
{
  "login": "string",
  "password": "string"
}
Response:
json
{
  "message": "Transaction added successfully"
}
GET /list: Retrieve a list of transactions.

Query Parameters:
user_id: The ID of the user whose transactions you want to retrieve.
Response: List of transactions.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

Feel free to customize this template to better fit the specifics of your project and any additional features you may have.







