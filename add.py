def add(a, b):
    """加法运算"""
    return a + b


def subtract(a, b):
    """减法运算"""
    return a - b


def multiply(a, b):
    """乘法运算"""
    return a * b


def divide(a, b):
    """除法运算，除零时抛出异常"""
    if b == 0:
        raise ZeroDivisionError("除数不能为零")
    return a / b
