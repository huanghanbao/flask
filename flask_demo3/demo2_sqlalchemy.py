# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建Flask 应用程序实例
app = Flask(__name__)
# 设置使用的数据库的链接地址：mysql://<username>:<password>@<host>:<port>/<database>
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mysql@192.168.105.137:3306/test1"
# 是否追踪数据库中数据的修改（新增，更新，删除）
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 在终端中回显sql语句
app.config['SQLALCHEMY_ECHO'] = True

# 创建数据库对象，跟当前app关联起来
db = SQLAlchemy(app)


# 一类
class Role(db.Model):
    """用户角色模型类"""
    # 指定表名
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)  # 设置主键，默认自动增长
    name = db.Column(db.String(64), unique=True, nullable=False)


def __repr__(self):
    return 'Role:%s  %s' % (self.id, self.name)


# 多类
class User(db.Model):
    """用户模型类"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)  # 设置主键，默认自动增长
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 设置外键

    def __repr__(self):
        return 'Role:%s  %s  %s  %s' % (self.name, self.email, self.password, self.role_id)


@app.route('/')
def index():
    return 'index'

"""
查询所有用户数据
User.query.all()

查询有多少个用户
User.query.count()

查询第1个用户
User.query.first()

查询id为4的用户[3种方式]
User.query.get(4)
User.query.filter_by().first()
User.query.filter(User.id == 4).first()

查询名字结尾字符为g的所有数据[开始/包含]
User.name.filter(User.name.endswith("g")).all()

查询名字不等于wang的所有数据[2种方式]
User.query.filter(User.name != 'wang').all()

from sqlalchemy import not_
User.query.filter(not_(User.name=='wang')).all()

查询名字和邮箱都以 li 开头的所有数据[2种方式]
User.query.filter(User.name.startswith('li'), User.email.startswith('li')).all()
from sqlalchemy import and_
User.query.filter(and_(User.name.startswith('li'), User.email.startswith('li'))).all()

查询password是 `123456` 或者 `email` 以 `itheima.com` 结尾的所有数据
from sqlalchemy import or_
User.query.filter(or_(User.password=='123456', User.email.startswith('itheima.com'))).all()

查询id为 [1, 3, 5, 7, 9] 的用户列表
User.query.filter(User.id.in_([1, 3, 5, 7, 9])).all()

查询name为liu的角色数据
User.query.filter(User.name.startswith("li"), User.email.startswith("li")).all()

查询所有用户数据，并以邮箱排序
降序
User.query.order_by(User.email.desc()).all()
升序
User.query.order_by(User.email.asc()).all()

每页3个，查询第2 页的数据
page = User.query.paginate(2, 3)

"""

if __name__ == "__main__":
    # 删除数据库表
    db.drop_all()
    # 生成数据库中表
    db.create_all()

    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='staff')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()

    app.run(debug=True)