# coding=utf-8
from flask import Flask, request

# 创建Flask应用程序实例
app = Flask(__name__)


@app.route('/')
def index():
    # # 请求方式
    # print request.method
    # # ip和端口
    # print request.url
    # # 添加的域名
    # print request.path

    # 获取查询的（字符串)
    a = request.args.get("a")
    b = request.args.get("b")

    return 'index-> a: %s b: %s' % (a, b)


# 演示是获取表单post提交的数据
@app.route("/demo0", methods=["POST"])
def demo():
    a = request.form.get("a")
    b = request.form.get("b")

    return "a: %s b: %s method: %s " % (a, b, request.method)


# 演示获取客户端请求的json数据
@app.route("/demo1", methods=["POST"])
def demo1():
    print request.data
    return "demo1"


# 演示接收客户端上传文件
@app.route("/upload", methods=["POST"])
def upload():
    # 获取上传文件的对象
    file = request.files.get("pic")

    # with open("./1.jpg", "wb") as f:
    #     f.write(file.read())
    #
    # return "success"

    file.save("./2.jpg")

if __name__ == "__main__":
    app.run(debug=True)
