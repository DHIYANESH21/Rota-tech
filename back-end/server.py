# app.py

from flask import Flask
from routes.user_routes import register_user_routes

app = Flask(__name__)

# Register the routes
register_user_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
