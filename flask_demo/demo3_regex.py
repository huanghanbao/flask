# coding=utf-8
from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# Flask和url相关底层类：
# BaseConverter子类：保存提取url参数匹配规则
# Rule类：记录一个url地址和一个视图函数的对应关系
# Map类：记录所有url地址和视图对应的关系
# MapAdapter类：执行url匹配过程的类

# 问题1：只能匹配6位数字，不能任意指定匹配的规则
# 问题2：提取的参数是一个字符串，不是数字
class RegexConverter(BaseConverter):
    # 指定匹配参数时正则表达式
    # regex = "\d{6}"

    def __init__(self, url_map, regex1):
        # 调用父类的方法
        super(RegexConverter, self).__init__(url_map)
        # 设置转换器中的匹配规则
        self.regex = regex1

    # 此方法在对应视图函数之前调用
    # 此方法在url地址中提取出参数之后，会先调用to_python,会把提取出的值作为参数传递给to_python
    # to_python的返回值最终会传递给对应视图参数
    # 在此方法中可以提取出的参数尽心处理，比如：类型转换
    def to_python(self, value):
        # return value
        # return "666666"
        return int(value)

    # 此方法是调用URl_for时会被调用
    # 调用to_url时会把反向解析中的url参数传递给to_url地址
    # url_for会利用to_url的返回值拼接来生成反向的url地址
    # 在此方法中可以对拼接url的参数进行处理：比如：将int转换成str
    def to_url(self, value):
        return str(value)
        # return '333333'


# 添加路由转换器
app.url_map.converters["re"] = RegexConverter


# @app.route("/order/<int:order_id">)
@app.route("/order/<re(r'\d{6}'):order_id>")
def demo0(order_id):
    return "order: %d" % order_id


@app.route("/redirect")
def demo1():
    url = url_for("demo0", order_id="666666")
    return redirect(url)


if __name__ == "__main__":
    print app.url_map
    app.run(debug=True)
