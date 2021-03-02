"""
python 编程基础
"""

# TODO 1、屏幕输入方法
# import sys
#
# a = next(sys.stdin)
# print("sys.stdin", a)
# b = input("int:")
# print('input', b)

# # TODO 2、for 断言assert与
# def hello():
#     try:
#         assert 1 + 1 == 21
#     except Exception:
#         print('111')
#         raise ValueError("值错误")
# hello()
# try:
#     int('a')
# except:
#     raise


# TODO 3、迭代器与生成器
a = '123abc'  # 迭代器，定义了iter()方法的对象，可以通过next()取值的对象，是一个迭代器。迭代，即从一个迭代器遍历元素
b = iter(a)
print(type(b))
print(next(b))
print(next(b))
for x in b:
    print('hello', x)


def yield_a():  # 生成器，生成器也是迭代器，可以迭代取值；他的作用主要体现在随取随用，减少内存占用消耗；
    print('生成器开始')
    for x in range(5):
        import random
        yield random.random()
    print('生成器结束')


print(next(yield_a()))
print(next(yield_a()))
for x in yield_a():
    print('hello', x)
print(list(yield_a()))


b=yield_a()
print(next(b))
print(next(b))
for x in b:
    print('hello', x)

yield_value = (x for x in range(10))
print(type(yield_value))
print(next(yield_value))
print(next(yield_value))
for x in yield_value:
    print('hello', x)