from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('puzzle.html')


@app.route('/image/<int:image_id>')
def get_image(image_id):

  return jsonify({'url': f'http://localhost/test{image_id}.png'})

if __name__ == '__main__':
  app.run()
