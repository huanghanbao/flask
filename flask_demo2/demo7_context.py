# coding=utf-8
from flask import Flask, request, session, current_app, g

# 创建Flask应用程序实例
app = Flask(__name__)
app.secret_key = '#$$hjgjk$%#$'

# Flask中包含两种上下文：
# 1、请求上下文：request  session
# 2、应用上下文：current_app  g

# 请求上下：在请求发生之后可以使用的变量
# 如果在请求之外使用会报错：working outside of request context
# print request.method
# session['name'] = "itcast"

# 应用上下文:在应用程序启动之后可以使用变量，可以设置和获取跟每次请求相关的信息
# 如果出错：RuntimeError: working outside of application context
# print current_app.secret_key


@app.route('/')
def index():
    # print request.url
    # session['name'] = "itcast"
    # #$$hjgjk$%#$  current_app跟app一下
    print current_app.secret_key
    return 'index'


if __name__ == "__main__":
    app.run(debug=True)
