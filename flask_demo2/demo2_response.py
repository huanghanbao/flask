# coding=utf-8
import json

from flask import Flask, jsonify
from flask import make_response
from flask import redirect
from flask import url_for

# 创建Flask应用程序实例
app = Flask(__name__)


@app.route('/')
def index():
    # 视图函数的返回值可以是一个元祖（content[响应体],status[状态码]，headers[响应头]）
    # 其中status和headers可以省略
    # return 'index', 666, {"Name": "Laowang"}

    # 通过response对象返回, 跟上面方法一样
    response = make_response("index")
    response.status_code = 200
    response.headers["Name"] = "XiaoHong"
    return response


@app.route("/redirect")
def demo0():
    # return redirect(url_for("index"))

    response = make_response()
    response.status_code = 302
    response.headers["Location"] = "http://127.0.0.1:5000/"
    return response


@app.route("/get_json")
def demo1():
    resp = {
        "name": "laowang",
        "age": 18
    }

    # # dumps把一个字典转换成json字符串
    # resp_json = json.dumps(resp)
    # # loads把json字符串转换成字典
    # resp_dict = json.loads(resp_json)
    # response = make_response(resp_json)
    # # 指定返回内容的类型是json
    # response.headers["Content-Type"] = "application/json"
    # return response

    return jsonify(resp)


if __name__ == "__main__":
    app.run(debug=True)
