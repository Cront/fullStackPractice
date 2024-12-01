# All database models
# Import the database object from the configuration file
from config import db

# Define the `Contact` model
# Represents the structure of the `Contact` table in the database
class Contact(db.Model):
    # Define the `id` column
    # Primary key for the table, an auto-incrementing integer
    id = db.Column(db.Integer, primary_key=True)
    
    # Define the `first_name` column
    # A string column with a maximum length of 80 characters, cannot be null, and is not required to be unique
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    
    # Define the `last_name` column
    # A string column with a maximum length of 80 characters, cannot be null, and is not required to be unique
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    
    # Define the `email` column
    # A string column with a maximum length of 120 characters, must be unique, and cannot be null
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Method to convert the `Contact` object into a JSON-compatible dictionary
    # Useful for sending or returning data as JSON in an API response
    def to_json(self):
        return {
            "id": self.id,                # Returns the `id` of the contact
            "firstName": self.first_name, # Returns the `first_name` as `firstName`
            "lastName": self.last_name,   # Returns the `last_name` as `lastName`
            "email": self.email           # Returns the `email` of the contact
        }
