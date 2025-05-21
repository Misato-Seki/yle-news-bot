from flask import Flask, send_from_directory
import os

app = Flask(__name__)
HTML_DIR = os.path.abspath('.')

@app.route('/')
def index():
    return send_from_directory(HTML_DIR, 'latest_summary.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)