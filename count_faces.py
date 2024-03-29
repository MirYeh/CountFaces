"""
This module uses https://github.com/shantnu/FaceDetect in order to recognize faces of images from the internet
Entry point - count_faces_from_weblink
"""
import requests

from api.face_detect import face_detect_cv3
from utils import clean_up, os

IMAGE_PATH = './images'


def download_image(image_link, title='random_img'):
    """ Download image from link and save it to IMAGES_PATH """
    response = requests.get(image_link)
    img_bytes = response.content
    image_path = f'{IMAGE_PATH}/{title}.jpg'
    os.save(image_path, img_bytes)
    return image_path


def count_faces(image_path):
    """ Count faces using 3rd party FaceDetect """
    return face_detect_cv3.run(image_path)


def delete_images():
    """ Deleting images after usage - used for cleanup """
    clean_up.delete_folder_content(IMAGE_PATH)


def count_faces_from_weblink(image_link, title='random_img'):
    """ Download image from the internet and count faces """
    image_path = download_image(image_link, title)
    return count_faces(image_path)
