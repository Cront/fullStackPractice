# configurations of the application
# for projects, start with base configurations

# Importing necessary libraries
# Flask: Lightweight web application framework
# Flask_SQLAlchemy: SQLAlchemy integration for Flask, used for database handling
# Flask_CORS: Enables Cross-Origin Resource Sharing for handling requests from different origins
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize the Flask application
# `Flask(__name__)` creates an instance of the Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for the app
# This allows your application to handle requests from different origins, useful for APIs
CORS(app)

# Configuring the application with database settings
# Specify the database connection URI; here, using SQLite with a database file named `mydatabase.db`
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# Disable the modification tracking feature of SQLAlchemy
# `SQLALCHEMY_TRACK_MODIFICATIONS` is set to `False` to save resources by not tracking object changes
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the SQLAlchemy object with the app
# This object (`db`) will allow you to interact with the database using ORM (Object-Relational Mapping)
db = SQLAlchemy(app)
