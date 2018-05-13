# coding=utf-8
from . import cart_blu

from flask import render_template
# 使用蓝图步骤:
# 1. 创建蓝图对象
# 2. 使用蓝图对象注册路由
# 3. 使用app注册蓝图对象


# 2.使用蓝图对象注册路由
# 在蓝图视图中使用模板文件时，会先去项目目录下的templates中去查找模板文件
# 如果查找到，就不会在去蓝图templates文件夹中去找
@cart_blu.route("/cart_info")
def cart_info():
    # return "cart_info"
    return render_template("cart_info.html")
