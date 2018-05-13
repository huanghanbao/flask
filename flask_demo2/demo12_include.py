# coding=utf-8
from flask import Flask, render_template


# 创建Flask应用程序实例
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("test4_include.html")


if __name__ == "__main__":
    app.run(debug=True)