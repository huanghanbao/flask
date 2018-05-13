# coding=utf-8
# 演示assert断言的使用


def divnum(a, b):
    """除法操作"""
    assert isinstance(a, int), "参数a必须为整数"
    assert isinstance(b, int), "参数b必须为整数"
    assert b != 0, "除数不能为0"
    return a / b


if __name__ == "__main__":
    # print divnum(10, 5)
    print divnum('a', 5)
