import json
import requests
import time
import os

URL = os.environ.get('URL', 'http://localhost:8080')


def upload_file(file_path):
    """Upload pdf file to tabula server (local server started before run this main_code)

    Args:
        file_path (string): path of pdf file

    Returns:
        string: file_id of the file that stored on tabula server. This field will use to access the file
    """
    url = f'{URL}/upload.json'
    files = open(file_path, 'rb')
    form_data = {'files[]':files}
    response = requests.post(url, files=form_data)
    data = response.json()
    return data[0]['file_id']


def get_file_info(file_id):
    """Get information of file by file_id

    Args:
        file_id (string): file_id of this file on tabula server

    Returns:
        int: number of pages in pdf file
    """
    url = f'{URL}/pdf/{file_id}/metadata.json'
    data = None
    while data is None:
        response = requests.get(url)
        data = response.json()
        time.sleep(2)
    page_count = data['page_count']
    return page_count


def delete_all_file():
    """Remove all files on tabula server after end
    """
    url = f'{URL}/documents/'
    response = requests.get(url)
    data = response.json()
    for item in data:
        delete_file(item['id'])


def delete_file(file_id):
    """Remove file on tabula server with file_id

    Args:
        file_id (string): file id of this file on tabula server
    """
    url = f'{URL}/pdf/{file_id}'
    response = requests.post(url, data={'_method': 'delete'})


def get_data_by_coords(coords, file_id):
    """Get text data from pdf by list of coordinate

    Args:
        coords (string): coordinates on the pdf from which we wan to extract information
        file_id (string): id file of pdf is stored on tabula server

    Returns:
        list: list of list data extracted
    """
    coords = json.dumps(coords)
    url = f'{URL}/pdf/{file_id}/data'
    response = requests.post(url, data={"coords":coords, "filename": ""})
    return response.json()