""" Entry point - runs Flask server on port 5000 """
from flask import Flask, request

from count_faces import count_faces_from_weblink

app = Flask(__name__)


@app.route('/')
def count_faces():
    """
    Counts faces of image from weblink.
    Expects request param `link`
    Example: http://localhost:5000?link={some-web-link}
    """
    image_link = request.args.get('link')
    face_count = count_faces_from_weblink(image_link)
    return f'Found {face_count} faces!'


if __name__ == '__main__':
    app.run()
