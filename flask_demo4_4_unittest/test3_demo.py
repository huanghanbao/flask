# coding=utf-8
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# 创建Flask应用程序实例
app = Flask(__name__)

# 设置数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@172.16.179.139:3306/test5'
# 关闭追踪数据库数据的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 设置SECRET_KEY
app.config['SECRET_KEY'] = '!*@(#(@#akdkla291(*(#*d'

# 创建SQLAlchemy对象
db = SQLAlchemy(app)


# 设计模型类
# 作者-图书
class Author(db.Model):
    """作者模型类"""
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    # 关联属性
    books = db.relationship('Book', backref='author', lazy='dynamic')


class Book(db.Model):
    """图书模型类"""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id')) # 设置外键


if __name__ == '__main__':
    # 清除数据表
    db.drop_all()
    # 创建数据表
    db.create_all()

    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老李')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()

    bk1 = Book(title='老王回忆录', author_id=au1.id)
    bk2 = Book(title='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(title='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(title='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(title='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()

    # 运行开发web服务器
    app.run(debug=True, port=5000)