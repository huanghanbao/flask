# coding=utf-8
from flask import Flask, render_template, flash
from flask import redirect
from flask import request
from flask import url_for
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 创建Flask应用程序实例
app = Flask(__name__)
app.config["SECRET_KEY"] = "!**#($((@dakflda912993#(*$*$"


# 定义一个wtf表单类
# 1. 对表单数据的进行验证
# 2. 进行csrf验证
# 默认Flask框架中没有csrf验证功能
class RegisterForm(FlaskForm):
    username = StringField("用户名:", validators=[DataRequired()])
    password = PasswordField("密码:", validators=[DataRequired()])
    password2 = PasswordField("重复密码:", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("注册")


@app.route("/demo1", methods=["GET", "POST"])
def wtf_form():
    # 创建表单类的对象
    form = RegisterForm()

    if request.method == "POST":
        # 进行注册处理
        if form.validate_on_submit():
            # 数据验证通过
            username = form.username.data
            password = form.password.data
            password2 = form.password2.data

            # 注册处理...
            print username, password, password2
            # 返回应答
            return redirect(url_for('index'))
        else:
            # 数据验证失败
            flash("数据错误")
            return "数据错误"
    return render_template("test1_wtf.html", form=form)


@app.route('/demo0', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 进行注册处理
        # 获取用户注册信息
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not all([username, password, password2]):
            flash("参数不完整")
            return "参数不完整"
        elif password != password2:
            flash("两次密码不一致")
            return "两次密码不一致"
        else:
            # 参数合法
            # 注册处理.....

            return "注册成功"

    return render_template("test1_wtf.html")

if __name__ == '__main__':
    # 运行开发web服务器
    app.run(debug=True)