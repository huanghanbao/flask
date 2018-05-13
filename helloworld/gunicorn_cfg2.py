# coding=utf-8
# 指定web服务器监听的ip和端口号
bind = "127.0.0.1:8002"
# 指定工作进程数
workers = 4
# 指定服务器后台运行
daemon = True
# 启动服务器之后生成gunicorn.pid, 保存主进程id
pidfile = 'gunicorn2.pid'
# 启动服务器之后生成access.log, 保存访问日志信息
accesslog = 'access2.log'
# 启动服务器之后生成error.log, 保存错误日志信息
errorlog = 'error2.log'