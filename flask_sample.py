from io import BytesIO
from os.path import basename

from flask import Flask, send_file
import requests
from scrape import scrape

app = Flask(__name__)


@app.route('/')
def hello_world():
    # localhost:8000/
    file_url = scrape()
    file = requests.get(file_url).content
    with open(basename('img.png'), "wb") as f:
        f.write(file)
    return send_file(f, mimetype='image/png')


if __name__ == '__main__':
    app.run()
