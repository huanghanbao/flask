# coding=utf-8
from flask import Flask, render_template


# 创建Flask应用程序实例
app = Flask(__name__)

# Django中使用过滤器：
# {{ 模板变量|过滤器："参数" }}

# Jinja2中使用过滤器：
# {{ 模板变量|过滤器：("参数1"，"参数2" ...)}}


# 自定义过滤器
# @app.template_filter("li_reverse")
def do_li_reverse(li):
    """反转列表元素"""
    temp = list(li)
    temp.reverse()
    return temp

app.add_template_filter(do_li_reverse, "li_reverse")


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
    return render_template("test2_filter.html", **context)


if __name__ == "__main__":
    app.run(debug=True)