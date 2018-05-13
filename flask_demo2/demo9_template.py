# coding=utf-8
from flask import Flask, render_template

# 创建Flask应用程序实例
app = Flask(__name__)


# Django使用模板变量的时候，无论是使用字典的键值、列表元素、对象的属性，都是通过.来使用的
# Jinja2模板中可以使用[]
# Jinja2模板变量可以直接进行算术运算
@app.route('/')
def index():
    my_dict = {
        "name": "laowang",
        "age": 18
    }
    my_li = [1, 3, 5, 7, 9]
    my_int = 2

    context = {
        "my_dict": my_dict,
        "my_li": my_li,
        "my_int": my_int

    }

    # return render_template("test1_temp.html", my_dict=my_dict, my_li=my_li, my_int=my_int)
    return render_template("test1_temp.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
