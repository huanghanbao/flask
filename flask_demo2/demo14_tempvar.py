# coding=utf-8
from flask import Flask, render_template, flash


# 创建Flask应用程序实例
app = Flask(__name__)
app.config["SECRET_KEY"] = "&^%^jkljghk$$%&"


@app.route('/')
def index():
    # 添加闪现消息
    flash(u"闪现消息1")
    flash(u"闪现消息2")
    flash(u"闪现消息3")
    flash(u"闪现消息4")

    return render_template("test6_tempvar.html")


if __name__ == "__main__":
    app.run(debug=True)