from backend import database
from pdf2image import convert_from_path
import numpy as np
import cv2
import os


def get_file_name(filepath):
    filename = os.path.split(filepath)[1]
    return filename.replace('.pdf', '').replace('.PDF', '')


def export_image(filepath, output_dir):
    filename = get_file_name(filepath)
    pages = convert_from_path(filepath, 72)
    for i in range(len(pages)):
        page = pages[i]
        image = np.array(page)
        image = image[:, :, ::-1].copy()
        image_path = os.path.join(output_dir, f'{filename}_{i+1}.png')
        cv2.imwrite(image_path, image)
    return (len(pages), image.shape[0], image.shape[1])
