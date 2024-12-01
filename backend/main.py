# main routes and endpoints

# create:
# - first_name
# - last_name
# - email

# Request
# type: GET, POST (create smthg new), PUT / PATCH (update smthg), DELETE
# json: {
# }

# Response
# status: 404 (not found), 400 (bad request), etc. 
# json: {
# }

# Import necessary modules
from flask import request, jsonify  # Used for handling HTTP requests and JSON responses
from config import app, db          # Import the Flask app and database from the config file
from models import Contact          # Import the Contact model for database interactions

# Define a route to retrieve all contacts
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # Query all contacts from the database
    contacts = Contact.query.all()
    
    # Convert the contacts to JSON using the `to_json` method for each contact
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    
    # Return a JSON response containing all contacts
    return jsonify({"contacts": json_contacts})

# Define a route to create a new contact
@app.route("/create_contact", methods=["POST"])
def create_contact():
    # Retrieve data from the JSON body of the POST request
    first_name = request.json.get("firstName")  # Extract the "firstName" field
    last_name = request.json.get("lastName")    # Extract the "lastName" field
    email = request.json.get("email")           # Extract the "email" field

    # Validate the presence of required fields
    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name, and email"}), 400

    # Create a new Contact instance
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    
    # Attempt to add the new contact to the database
    try:
        db.session.add(new_contact)  # Add the new contact to the session
        db.session.commit()          # Commit the changes to the database
    except Exception as e:
        # Handle database errors and return a 400 status with the error message
        return jsonify({"message": str(e)}), 400

    # Return a success message with a 201 status (resource created)
    return jsonify({"message": "User created!"}), 201

# Define a route to update an existing contact
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    # Retrieve the contact by its ID
    contact = Contact.query.get(user_id)

    # Check if the contact exists
    if not contact:
        return jsonify({"message": "User not found"}), 404

    # Retrieve data from the JSON body of the PATCH request
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)  # Update first name if provided
    contact.last_name = data.get("lastName", contact.last_name)     # Update last name if provided
    contact.email = data.get("email", contact.email)                # Update email if provided

    # Commit the changes to the database
    db.session.commit()

    # Return a success message with a 200 status
    return jsonify({"message": "User updated!"}), 200

# Define a route to delete a contact
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    # Retrieve the contact by its ID
    contact = Contact.query.get(user_id)

    # Check if the contact exists
    if not contact:
        return jsonify({"message": "User not found"}), 404

    # Delete the contact from the database
    db.session.delete(contact)
    db.session.commit()

    # Return a success message with a 200 status
    return jsonify({"message": "User deleted!"}), 200

# Entry point for running the application
if __name__ == '__main__':
    # Ensure that the app context is available for database operations
    with app.app_context():
        db.create_all()  # Create all tables in the database if they do not already exist

    # Start the Flask application in debug mode
    app.run(debug=True)
