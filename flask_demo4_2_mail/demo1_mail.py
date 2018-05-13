# coding=utf-8
import threading
from flask import Flask
# pip install flask-mail
from flask_mail import Mail, Message

# 创建Flask应用程序实例
app = Flask(__name__)

# 配置邮件：服务器／端口／安全套接字层／邮箱名／授权码
app.config['MAIL_SERVER'] = "smtp.163.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "qq470457699@163.com"
app.config['MAIL_PASSWORD'] = "python8"
# 默认发件人
app.config['MAIL_DEFAULT_SENDER'] = 'FlaskAdmin<qq470457699@163.com>'

# 创建Mail对象
mail = Mail(app)


@app.route('/')
def index():
    return 'index'

# celery本质: 找一个进程帮我们调用发送邮件的函数。
# celery: 任务发送者， 中间人， 任务处理者 可以在不同电脑上
# celery会对任务排队

# f = open("file", 'wb')
# f.write("dkdkkdkd")
# f.close()
#
# with open("file", "wb") as f:
#     f.write("dddkdkdkkd")


def async_send_mail():
    # 手动开启应用上下文
    with app.app_context():
        # 创建Message
        message = Message("邮件标题", recipients=["qq470457699@163.com"])
        # message.body = "我是邮件内容"
        message.html = "<h1>我是邮件内容</h1>"
        # 发送邮件
        import time
        time.sleep(5)
        mail.send(message)


@app.route("/send_mail")
def send_mail():
    """发送邮件"""
    # # 创建Message
    # message = Message("邮件标题", recipients=["smartli_it@163.com"])
    # # message.body = "我是邮件内容"
    # message.html = "<h1>我是大标题</h1>"
    # # 发送邮件
    # mail.send(message)

    # 发邮件
    thread = threading.Thread(target=async_send_mail)
    thread.start()

    return "send mail..."

if __name__ == '__main__':
    # 运行开发web服务器
    app.run(debug=True)