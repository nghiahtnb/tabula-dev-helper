from project import db
from datetime import datetime


class Data(db.Model):
    __tablename__ = "data"

    file_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file_name = db.Column(db.String(128), nullable=False)
    date_create = db.Column(db.DateTime, nullable=False)
    number_pages = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    is_delete = db.Column(db.Boolean, nullable=False)

    def __init__(self, file_name, number_pages, height, width):
        self.file_name = file_name
        self.date_create = datetime.now()
        self.number_pages = number_pages
        self.height = height
        self.width = width
        self.is_delete = False


def count_data():
    num_rows = db.session.query(Data).count()
    return num_rows


def insert_data(file_name, number_pages, height, width):
    data = Data(file_name, number_pages, height, width)
    db.session.add(data)
    db.session.commit()

