from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('puzzle.html')


@app.route('/image/<int:image_id>')
def get_image(image_id):
    # In a real application, you would use the image_id parameter to look up the
    # corresponding image in your server's storage and return it to the client.
    # For this example, we'll just return a dummy response.

    return jsonify({'url': f'http://localhost/test/con%20{image_id}.png'})


if __name__ == '__main__':
    app.run()
