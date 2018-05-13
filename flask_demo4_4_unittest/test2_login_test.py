# coding=utf-8
import unittest
import json
from test2_login import app


class TestLoginCase(unittest.TestCase):
    # 需求: 测试登录时参数不完整的情况，结果是否符合预期
    # 预期结果: 返回Json errcode = -2
        # 1. 只传递用户名
        # 2. 只传递密码
        # 3. 用户名和密码都没传
    def setUp(self):
        # 此函数在测试函数执行之前会自动被调用，可以在此函数中做一些测试之前初始化的工作
        client = app.test_client()
        self.client = client
        # 开启Flask测试的模式
        # 如果开启测试模式，当被测试的目标代码出错时，会直接定位到目标代码错误代码位置
        # 如果未开启测试模式，当被测试的目标代码出错时，只会显示测试代码的错误，而不会定位到目标代码错误代码位置
        app.testing = True

    def test_empty_username_password(self):
        # 创建Flask测试客户端对象
        # client = app.test_client()

        # post请求/login
        response = self.client.post("/login", data={"username": "itheima"})
        # 获取返回的数据
        res_data = response.data
        # 将json字符串转换成python字典
        res_dict = json.loads(res_data)

        self.assertIn("errcode", res_dict, "errcode not in json data")
        errcode = res_dict.get("errcode")
        real_errcode = -2
        self.assertEqual(errcode, real_errcode,
                         "errcode should be %s, not %s" %(real_errcode, errcode))

    def test_error_username_password(self):
        # 创建Flask测试客户端对象
        # client = app.test_client()

        # post请求/login
        response = self.client.post("/login", data={"username": "itheima", "password": "123"})
        # 获取返回的数据
        res_data = response.data
        # 将json字符串转换成python字典
        res_dict = json.loads(res_data)

        self.assertIn("errcode", res_dict, "errcode not in json data")
        errcode = res_dict.get("errcode")
        real_errcode = -1
        self.assertEqual(errcode, real_errcode,
                         "errcode should be %s, not %s" % (real_errcode, errcode))