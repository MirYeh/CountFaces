import json
import os
import unittest

import count_faces


class CountFacesTest(unittest.TestCase):
    IMAGE_URL = 'https://peopledotcom.files.wordpress.com/2018/12/books-8.jpg?crop=0px%2C13px%2C2700px%2C1419px&resize=1200%2C630'
    IMAGES_RESOURCE_PATH = './resources/images.json'

    def test_download_image(self):
        link = self.IMAGE_URL
        image_path = count_faces.download_image(link, title='test_img')
        self.assertTrue(os.path.exists(image_path))
        count_faces.delete_images()

    def test_count_faces(self):
        cwd = os.getcwd()
        with open(self.IMAGES_RESOURCE_PATH, 'r') as f:
            images_resource = json.loads(f.read())
            for image_resource in images_resource:
                face_count = count_faces.count_faces(f'{cwd}/{image_resource.get("image")}')
                expected = int(image_resource.get('faces'))
                self.assertEqual(face_count, expected, f'expected {expected} faces, got {face_count}')


if __name__ == '__main__':
    unittest.main()
