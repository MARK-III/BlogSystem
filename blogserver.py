from flask import Flask
from flask import request
from flask import send_from_directory

app = Flask(__name__, static_url_path='/html')

@app.route('/<name>')
def index(name):
    if name == '':
        return app.send_static_file('index.html')

    else:
        return app.send_static_file(name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.0.93',port=10090)
