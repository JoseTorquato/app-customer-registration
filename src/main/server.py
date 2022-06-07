from flask import Flask
from flask_cors import CORS

from .routes import customer_registration_routes_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(customer_registration_routes_bp)
