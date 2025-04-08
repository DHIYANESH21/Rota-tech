from flask import Flask, jsonify
from pymongo import MongoClient
app = Flask(__name__)
MONGO_URI="mongodb+srv://kabilrsit:awcgkyuCJCgmStHy@projects.vifrcka.mongodb.net/"
client = MongoClient(MONGO_URI)
try:
    client.admin.command('ping')
    print("✅ MongoDB connection successful!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
db = client['mydatabase']
collection = db['users']
@app.route('/')
def home():
    return "Flask + MongoDB Atlas is working!"
@app.route('/users')
def get_users():
    users = list(collection.find({}, {'_id': 0}))  
    return jsonify(users)
if __name__ == '__main__':
    app.run(debug=True)
