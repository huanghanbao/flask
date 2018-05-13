# coding=utf-8
from flask import Flask, session


# 创建Flask应用程序实例
app = Flask(__name__)
app.secret_key = '#$$hjgjk$%#$'


@app.route('/')
def index():
    return 'index'


@app.route("/set_session")
def set_session():
    # 如果不设置过期时间，默认关闭浏览器过期
    # 设置session过期时间
    session.permanent = True
    app.permanent_session_lifetime = 3600   # 秒

    session["name"] = "xiaohong"
    session["age"] = 18
    return "设置session信息"


@app.route("/get_session")
def get_session():
    name = session.get("name", "")
    age = session.get("age", "")
    return "获取session信息：name：%s / age：%s" % (name, age)


@app.route("/del_session")
def del_session():
    # 删除和客户端相关的所有session
    # session.clear()

    # 删除某一个session
    session.pop("name")

    return "清除session信息"

if __name__ == "__main__":
    app.run(debug=True)