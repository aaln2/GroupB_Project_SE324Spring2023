import unittest

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/image/<int:image_id>')
def get_image(image_id):
    # In a real application, you would use the image_id parameter to look up the
    # corresponding image in your server's storage and return it to the client.
    # For this example, we'll just return a dummy response.
    return jsonify({'url': f'http://localhost/test/con%20{image_id}.jpg'})


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Add more tests for the index page as needed

    def test_get_image(self):
        response = self.app.get('/image/1')
        self.assertEqual(response.status_code, 200)
        # Add more tests for the get_image endpoint as needed


if __name__ == '__main__':
    app.run()
