#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask import request
from flask import send_from_directory
from flask import url_for
from flask import redirect

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.93', port=80, threaded=True)
