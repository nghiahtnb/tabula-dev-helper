import os


# basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_FOLDER = os.getenv('APP_FOLDER', '.')
    STATIC_FOLDER = f"{APP_FOLDER}/project/static"
    UPLOAD_FOLDER = f"{APP_FOLDER}/project/static/uploads"
    RESULT_FOLDER = f"{APP_FOLDER}/project/static/results"
