# coding=utf-8
import unittest
from test3_demo import app
from test3_demo import db, Author
# 需求: 写一个测试案例，测试向authors表中添加数据是否成功


class TestDBCase(unittest.TestCase):
    def setUp(self):
        # 设置测试数据库链接地址
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@172.16.179.139:3306/testcase'
        db.create_all()
        # 开启测试模式
        app.testing = True

    def test_insert_author_data(self):
        author = Author(name="laowang")
        db.session.add(author)
        db.session.commit()

        import time
        time.sleep(15)
        author = Author.query.filter(Author.name == "laowang").first()
        self.assertIsNotNone(author, "insert author data error")

    def tearDown(self):
        # 此函数在所有测试代码执行之后被自动调用，可以在此函数中做一些测试之后做一些清理工作
        db.session.close()
        db.drop_all()
