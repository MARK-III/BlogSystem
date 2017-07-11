#coding:utf-8
import sys
import os
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
    return redirect('/blog')

@app.route('/blog')
def blog_index():
    return send_from_directory('Blog/html', 'index.html')

@app.route('/blog/<filename>')
def blog_article(filename):
    return send_from_directory('Blog/html', filename)

@app.route('/pic/<filename>')
def pic(filename):
    return send_from_directory('Blog/pic', filename)

@app.route('/css/<filename>')
def css(filename):
    return send_from_directory('Blog/css', filename)


if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.101', port=80, threaded=True)
