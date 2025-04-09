# routes/user_routes.py

from flask import request, jsonify
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb+srv://tskailash20:tskailashts0807%40%40@cluster0.io3sx5a.mongodb.net/edu_tech?retryWrites=true&w=majority&appName=Cluster0')
db = client['mydatabase']
collection = db['users']

def register_user_routes(app):

    @app.route('/add_user', methods=['POST'])
    def add_user():
        try:
            data = request.get_json(force=True)
            name = data.get('name')
            age = data.get('age')

            if not name or not age:
                return jsonify({"error": "Missing data"}), 400

            collection.insert_one({"name": name, "age": age})
            return jsonify({"message": "User added successfully"}), 201

        except Exception as e:
            return jsonify({"error": f"Failed to add user: {str(e)}"}), 500

    @app.route('/users', methods=['GET'])
    def get_users():
        users = list(collection.find({}, {"_id": 0}))
        return jsonify(users)
