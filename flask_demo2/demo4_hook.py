# coding=utf-8
from flask import Flask

# 创建Flask应用程序实例
app = Flask(__name__)


# before_first_request:服务器启动之后，接收第一个请求时调用
# 可以在这个钩子函数中做一些项目初始化的工作，建立数据的链接
@app.before_first_request
def before_first_request():
    print "before_first_request"


# before_request：视图函数调用之前被调用
# 可以在这个钩子函数中做一些请求的校验工作：1 禁止某些ip访问网站  2 csrf验证
@app.before_request
def before_request():
    print "before_request"
    # if ip在黑名单中：
    # return "不能访问"

    # if csrf验证失败：
    # return "Forbidden"


# after_request：在每次请求时，视图函数调用之后（如果视图没有异常）被调用
# 在此钩子函数中可以做一些返回之前的数据处理：比如：统一设置返回给浏览器的内容的Content—Type
# 每一个返回的数据都是json
@app.after_request
def after_request(response):
    print "after_request"
    response.headers["Content-Type"] = "application/json"
    return response


# teardown_request：在每次请求时，视图函数调用之后（不管有没有异常）都会被调用
# 如果发生异常，异常对象会作为参数传递给钩子函数
@app.teardown_request
def teardown_request(e):
    print "teardown_request：%s" % e


@app.route('/')
def index():
    print "index"
    # num = 10 / 0
    return 'index'


@app.route('/index2')
def index2():
    print "index2"
    return 'index2'


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()