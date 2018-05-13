

def func_decorator(func):
    def wrapper(a, b):
        print "add wrapper"
        return func(a, b)
    return wrapper


# 语法糖
# @func_decorator
def add(a, b):
    print "add"
    return a + b

# add = func_decorator(add)


if __name__ == "__main__":
    add = func_decorator(add)
    add(2, 3)
