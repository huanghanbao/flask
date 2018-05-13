# coding=utf-8
from flask import Flask
from flask_script import Manager

# 创建Flask应用程序实例
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run(debug=True)