# main entry to the system
from flask import Flask

# create flask object
app = Flask(__name__)


from application import routes