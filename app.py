from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '第一次运行'


if __name__ == '__main__':
    app.run()
