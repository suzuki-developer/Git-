import os

DEBUG = True

APP_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI  = 'sqlite:/// + os.path.join'(APP_DIRECTORY, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED     = True
CSRF_SESSION_KEY = ""
SECRET_KEY       = ""
