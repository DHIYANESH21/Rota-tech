from flask import Flask, request, jsonify
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('mongodb+srv://tskailash20:tskailashts0807%40%40@cluster0.io3sx5a.mongodb.net/edu_tech?retryWrites=true&w=majority&appName=Cluster0')
db = client['mydatabase']
collection = db['users']  
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.get_json(force=True)
        name = data.get('name')
        age = data.get('age')
        if not name or not age:
            return jsonify({"error": "Missing data"}), 400
        user = {"name": name, "age": age}
        collection.insert_one(user)
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Failed to add user: {str(e)}"}), 500
@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return jsonify(users)
if __name__ == '__main__':
    app.run(debug=True)
