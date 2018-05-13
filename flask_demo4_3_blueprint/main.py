# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
from users import user_info
from orders import order_blu
from cart import cart_blu
# 创建Flask应用程序实例
app = Flask(__name__)

# 循环引用: 让其中一方延迟导入或者不导入
app.route("/user_info")(user_info)

# 3. 使用app对象注册蓝图
app.register_blueprint(order_blu)
app.register_blueprint(cart_blu, url_prefix="/cart")


@app.route('/')
def index():
    return 'index'


# 用户模块
# 以下代码抽取到users.py文件中
# @app.route("/user_info")
# def user_info():
#     return "user_info"


# 订单模块
# 以下代码抽到到orders.py文件中
# @app.route("/order_info")
# def order_info():
#     return "order_info"


if __name__ == '__main__':
    # 运行开发web服务器
    print app.url_map
    app.run(debug=True)