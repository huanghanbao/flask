# coding=utf-8
from flask import Flask
from flask import make_response
from flask import request


# 创建Flask应用程序实例
app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/set_cookie')
def set_cookie():
    # 创建response对象
    response = make_response("设置cookie信息")

    # 设置cookie信息
    # response.set_cookie("name", "itcast", max_age=3600)
    # return response

    response.headers["Set-Cookie"] = "name=itheima; Expires=Tue, 08-May-2018 10:14:09 GMT; Max-Age=3600; Path=/"
    return response


@app.route("/get_cookie")
def get_cookie():
    # 获取cookie信息
    name = request.cookies.get("name", "")  # 第二个参数是默认值，默认返回None
    return u"获取cookie信息：name: %s" % name


@app.route("/del_cookie")
def del_cookie():
    # 删除cookie信息
    # 创建response对象
    response = make_response("删除cookie信息")
    response.delete_cookie("name")
    return response

if __name__ == "__main__":
    app.run(debug=True)
