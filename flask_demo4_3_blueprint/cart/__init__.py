# coding=utf-8
from flask import Blueprint

# 1.创建蓝图对象
cart_blu = Blueprint("cart", __name__,
                     template_folder="templates",  # 设置蓝图中模板目录
                     static_folder="static",  # 设置蓝图中静态文件目录
                     static_url_path="/static",  # 设置访问蓝图中静态文件url地址的前缀
                     # url_prefix="/cart",  # 设置蓝图中所有视图的url地址的前缀
                     )

from . import views
