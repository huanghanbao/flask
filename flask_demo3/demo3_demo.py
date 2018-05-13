# coding=utf-8
from flask import Flask, render_template
from flask import flash
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

# 创建Flask应用程序实例
app = Flask(__name__)
app.config["SECRET_KEY"] = "%^^&55687%$*%$"
# 指定使用的数据库的连接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mysql@192.168.105.137:3306/test2"
# 关闭追踪数据库的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 创建一个SQLAlchemy对象
db = SQLAlchemy(app)


# 定义表单类
class AuthorBookForm(FlaskForm):
    author_name = StringField(u'作者:', validators=[DataRequired()])
    book_btitle = StringField(u'图书:', validators=[DataRequired()])
    submit = SubmitField(u'添加')


# 定义作者和图书的模型类
class Author(db.Model):
    """作者模型类"""
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)  # 设置主键，自动增长
    name = db.Column(db.String(64), unique=True, nullable=False)
    books = db.relationship("Book", backref="author", lazy="dynamic")  # 关联属性


class Book(db.Model):
    """图籍类"""
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)  # 设置主键，自动增长
    title = db.Column(db.String(64), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)  # 外键


@app.route('/')
def index():
    # 创建表单类对象
    form = AuthorBookForm()
    # 获取所有作者的信息
    authors = Author.query.all()

    return render_template('test2.demo.html', authors=authors, form=form)


@app.route('/create', methods=["GET", 'POST'])
def create_book():
    # 添加图书和作者
    form = AuthorBookForm()
    if form.validate_on_submit():
        # 数据合法,获取数据
        author_name = form.author_name.data
        book_title = form.book_btitle.data

        # 查询作者是否存在
        author = Author.query.filter(Author.name == author_name).first()
        if author is None:
            # 添加新作者
            author = Author(name=author_name)
            db.session.add(author)
            db.session.commit()

        # 查询作者是否有这本图书
        book = Book.query.filter(Book.title == book_title, Book.author_id == author.id).first()
        if book is None:
            # 添加新图书
            book = Book(title=book_title, author_id=author.id)
            db.session.add(book)
            db.session.commit()
    else:
        # 数据不合法
        flash(u'数据不合法')
    # 重定向到首页
    return redirect("/")


@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    # 删除图书信息
    book = Book.query.get(book_id)

    db.session.delete(book)
    db.session.commit()
    # 重定向到首页
    return redirect("/")

if __name__ == "__main__":
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()

    # 添加测试数据
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

    app.run(debug=True)
