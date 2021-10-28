from flask import Flask, request, flash
from flask_sqlalchemy import SQLAlchemy
import os

from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

from backend import database, extraction


def create_folder():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])


def allow_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['pdf']


create_folder()

@app.route('/')
def default():
    return "Hello world!"


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return 'No selected file'
    if allow_file(file.filename):
        file_id = database.count_data() + 1
        filename = secure_filename(file.filename)
        filename = f"{file_id}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        res = extraction.export_image(filepath, app.config['UPLOAD_FOLDER'])
        database.insert_data(filename, res[0], res[1], res[2])
        print('Upload done')
        return {'status': 'SUCCESS', 'file_id': file_id}
    return 'Bad request', 400
