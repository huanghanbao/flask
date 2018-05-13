# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 演示数据库迁移
# python manage.py db init 进行数据库迁移管理初始化的工作，生成迁移文件

# 创建Flask 应用程序实例
app = Flask(__name__)
# 设置使用的数据库的链接地址：mysql://<username>:<password>@<host>:<port>/<database>
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:mysql@192.168.105.137:3306/test_migrate"
# 是否追踪数据库中数据的修改（新增，更新，删除）
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 创建数据库对象，跟当前app关联起来
db = SQLAlchemy(app)

# 创建一个Manager类对象
manager = Manager(app)
# 创建Migrate对象，传入app和db对象，使用迁移的方式管理当前app项目的数据库
Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 一类
class Role(db.Model):
    """用户角色模型类"""
    # 指定表名
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)  # 设置主键，默认自动增长
    name = db.Column(db.String(64), unique=True, nullable=False)

    users = db.relationship("User", backref="role", lazy="dynamic")


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

if __name__ == "__main__":
    # app.run()
    manager.run()