import os

class Config(object):
    # keeps information secure
    SECRET_KY = os.environ.get('SECRET_KY') or "secret_string"

