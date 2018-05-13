# coding=utf-8
from flask import Flask
from flask import abort

# 创建Flask应用程序实例
app = Flask(__name__)


@app.route('/')
def index():
    # 调用abort函数可以抛出一个指定错误码对应的异常信息
    # abort函数会立即终止当前视图函数的运行
    abort(404)
    return 'index'


@app.errorhandler(404)
def page_not_found(e):
    return "这是一个404页面：%s" % e

if __name__ == "__main__":
    app.run(debug=True)