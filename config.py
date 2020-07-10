import os


class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'tpYD7#NUUjB4yE&p3Z2Jn!SpMC5Qg3'
