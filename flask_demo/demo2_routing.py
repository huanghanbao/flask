# coding=utf-8
from flask import Flask, redirect
from flask import url_for

app = Flask(__name__)


def add(a, b):
    """加法"""
    return a + b


@app.route("/", methods=["get", "POST"])
@app.route("/index")
def index():
    a = 1
    b = 2
    c = add(a, b)
    print c
    return "index"


@app.route("/")  # 默认支持HEAD, OPTIONS
def index2():
    return "index2"


@app.route("/order/<int:order_id>")
def demo0(order_id):
    return "order: %s" % order_id


@app.route("/redirect")
def demo1():
    # 反向解析生成index视图对应的url地址
    # url = url_for("index")
    # return redirect(url)
    return redirect(url_for("demo0", order_id=555555))


# 只能匹配里面其中一个
@app.route("/<any(about, help, imprint, class, 'foo,bar'):page_name>")
def demo2(page_name):
    return page_name


# 加path可以提取路径，不加只能提取单个字符串
@app.route("/<path:name>")
def demo3(name):
    return name

if __name__ == '__main__':
    # 记录所有url地址和视图相对相应的关系
    print app.url_map
    app.run(debug=True)
