import os

class Config(object):
    # keeps information secure
    SECRET_KY = os.environ.get('SECRET_KY') or "secret_string"

    MONGODB_SETTINGS = {
        'db':'UTA_Enrollment',
        'host':'mongodb://localhost:27017/UTA_Enrollment'
    }
