import pymongo
import bcrypt

# Initialize MongoDB client with your MongoDB Atlas connection string
client = pymongo.MongoClient("mongodb+srv://adminbidan:adminbidan@cluster0.kuxrorf.mongodb.net/?retryWrites=true&w=majority")

# Connect to the 'mydb' database
db = client.mydb

# Connect to the 'users' collection
users_collection = db.users

def main(args):
    email = args.get('email')
    password = args.get('password')

    if not email or not password:
        return {"body" : {'message': 'Email & password needed'}}
        

    # Retrieve the user's data from MongoDB
    user_data = users_collection.find_one({'email': email})

    if not user_data:
        return {"body" : {'message': 'User not found'}}

    # Verify the password using bcrypt
    stored_password = user_data.get('password')

    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        return {"body" : {'message': 'Login successful'}}
    else:
        return {"body" : {'message': 'Incorrect password'}}