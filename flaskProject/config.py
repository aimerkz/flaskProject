import os

from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('TRACK_MODIFICATIONS')
    SECRET_KEY = os.getenv('SECRET_KEY')
    EXPLAIN_TEMPLATE_LOADING = False
