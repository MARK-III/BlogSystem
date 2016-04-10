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
    return redirect(url_for('blog'))

@app.route('/blog')
def blog():
    return redirect(url_for('static', filename='index.html'))
