# main entry to the system
from flask import Flask

# create flask object
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello World! This is functioning properly!?!?!</h1>"