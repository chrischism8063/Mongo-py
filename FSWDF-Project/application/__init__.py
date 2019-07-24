# main entry to the system
from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

# create flask object
app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from application import routes