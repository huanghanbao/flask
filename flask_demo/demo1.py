# coding=utf-8
from flask import Flask, render_template

# 创建Flask应用程序实例对象
# 如果模块存在，会根据模块所在的目录去寻找静态文件和模块名
# 如果模块不存在，会默认使用app对象所在的模块目录
app = Flask(__name__,  # 指定app对象所在的模块名
            static_folder="static",  # 指定静态文件存放目录，STATICFILES_DIRS
            static_path="/abc",  # 指定访问静态文件的url地址前缀，STATIC_URL
            template_folder="templates",  # 指定模板文件的目录

            )


# 项目配置
class Config(object):
    DEBUG = True

# # 配置方式1：通过配置类加载配置
# app.config.from_object(Config)

# 设置当前配置项
# app.config["DEBUG"] = True


# url地址和视图对应的关系
@app.route("/")
def index():
    # return 'hello world'
    return render_template("index.html")


if __name__ == '__main__':
    # 启动开发的web服务器
    # 参数1：ip，参数2：端口，参数3：设置当前配置项效果一样
    app.run(host="127.0.0.1", port=8001, debug=True)
