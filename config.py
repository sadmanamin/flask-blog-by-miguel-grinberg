import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ext.sadman.amin@bracu.ac.bd'
    MAIL_PASSWORD = 'Sadony1910'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    ADMINS = ['ext.sadman.amin@bracu.ac.bd']
    POSTS_PER_PAGE = 3
    