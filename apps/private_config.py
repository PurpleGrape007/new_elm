import os


DEBUG = True

SERVER_NAME = 'elm.com:5000'

SECRET_KEY = 'welcome'

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_name = os.path.join(base_dir, 'clm.db')

SQLALCHEMY_DATABASE_URI = r'sqlite:///{}'.format(db_name)

SQLALCHEMY_TRACK_MODIFICATIONS = True

EXPIRES_TIME = 30 * 24 * 3600

from redis import Redis


SESSION_TYPE = "redis"

SESSION_REDIS = Redis(host='192.168.102.128', port=6388)
