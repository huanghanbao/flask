# coding=utf-8
from flask import Blueprint

# 1.创建蓝图对象
order_blu = Blueprint("order", __name__)


# 2. 使用蓝图对象注册路由
@order_blu.route("/order_info")
def order_info():
    return "order_info"
