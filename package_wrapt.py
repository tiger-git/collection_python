# 参考：
# https://www.cnblogs.com/cicaday/p/python-decorator.html

# 前言：装饰器了解
# def drink(thing='啤酒'):
#     print(F"{drink.__name__}喝{thing}")
#     return len(thing)


# drink()
# TODO 装饰器功能:不改变原函数调用方式，增加功能或封装
# 注:
# １、将该函数及参数传入一个帽子函数（装饰器函数）进行处理，用处理后返回的参数继续执行业务（亦可返回原有参数）
# ２、除装饰函数，亦可装饰类实例方法、静态方法、类方法，如：
#
# def who(func):
#     def hello(*args, **kwargs):
#         print(F"原函数{func.__name__}参数为:{args},{kwargs}")
#         return func(*args, **kwargs)
#
#     return hello
#
#
# class Persion(object):
#     @who
#     def __init__(self, name, age):
#         pass
#
#     @who
#     def run(self, mile):
#         pass
#
#     @staticmethod
#     @who
#     def get_time(time_str):
#         pass
#
#     @classmethod
#     @who
#     def get_persion(cls, sex):
#         pass
#
#     @classmethod
#     @who
#     def get_human(cls, sex):
#         return cls('某某某', '万岁')
#
#
# # Persion('tiger',20)
# # Persion('tiger', 20).run(100)
# # Persion.get_time("2020-2-14")
# # Persion.get_persion("男")
# # Persion.get_human("男")
#
# # TODO 第１个装饰器
# def who_drink(func):
#     # TODO 获取原函数的形参及位参默认值
#     import inspect
#     data = inspect.getargspec(func)
#     key = data[0]
#     value = data[-1]
#     if value:
#         len_v = len(value)
#         args = tuple(key[:-len_v])
#         kwargs = {key[-(len_v - i)]: v for i, v in enumerate(value)}
#     else:
#         args = key
#         kwargs = {}
#     print(args, kwargs)
#
#     def hello(*args, **kwargs):
#         """
#         hello
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         print(F"函数{func.__name__}入参为：{args},{kwargs}")
#         print('今天喝什么？')
#         return func(*args, **kwargs)
#
#     return hello
#
#
# @who_drink  # 增加＠包装函数名
# def drink(thing='123', **kwargs):
#     """
#     drink
#     :param thing:
#     :param kwargs:
#     :return:
#     """
#     # print(F"{drink.__name__}喝what")
#     print(F"{drink.__name__}喝{thing}")
#     return


# ＠who_drink等同who_drink(drink)()
# who_drink(drink)()
# drink()
# drink('果1汁',a=1)
# print(drink.__name__)# @wraps(func)
# print(drink.__doc__)# @wraps(func)


# # TODO 第２个装饰器，@wraps(func) 解决函数名、函数文档字符等无法获取或对应问题
# from functools import wraps
#
#
# def who_drink(func):
#     @wraps(func)
#     def hello(*args, **kwargs):
#         """
#         hello hello
#         :param thing:
#         :return:
#         """
#         print(F"函数{func.__name__}入参为：{args},{kwargs}")
#         print('今天喝什么？')
#         return func(*args, **kwargs)
#
#     return hello
#
#
# @who_drink
# def drink(thing='啤酒'):
#     """
#     hello drink
#     :param thing:
#     :return:
#     """
#     print(F"喝{thing}")
#     return
#
# # print(drink.__name__)
# # print(drink.__doc__)
# # import inspect
# # print(inspect.getsource(drink))
# # print(inspect.getargspec(drink))
#
# # who_drink(drink)()
# drink()


# #TODO　第三个装饰器,@wrapt.decorator,解决函数参数签名等获取问题，同时也美化装饰器，增强易读性
# import wrapt  # 第三方包
#
#
# @wrapt.decorator
# def who_drink(func, instance, args, kwargs):
#     import inspect
#     # print(inspect.getargspec(func))
#     print(inspect.stack())
#     print(F"函数{func.__name__}入参为：{args},{kwargs}")
#     print('今天喝什么？')
#     return func(*args, **kwargs)
#
#
# @who_drink
# def drink(thing='啤酒'):
#     """
#     hello drink3
#     :param thing:
#     :return:
#     """
#     print(F"喝{thing}")
#     return
#
# # print(drink.__name__)
# # print(drink.__doc__)
# import inspect
# # print(inspect.getsource(drink))
# # print(inspect.getargspec(drink))
#
# drink()


# # TODO 带参数的装饰器（原理，返回一个装饰器即可，以上三种皆是）
#
#
# import wrapt
#
#
# def who_drink(diff=False):
#     @wrapt.decorator
#     def param(func, instance, args, kwargs):
#         import inspect
#         # print(inspect.getargspec(func))
#         print(inspect.stack())
#         print(F"函数{func.__name__}入参为：{args},{kwargs}")
#         print('今天喝什么？')
#         if diff:
#             kwargs['hello'] = 'world'
#         return func(*args, **kwargs)
#
#     return param
#
#
# @who_drink(True)
# def drink(thing='啤酒',**kwargs):
#     """
#     hello drink3
#     :param thing:
#     :return:
#     """
#     print('kwargs',kwargs)
#     print(F"喝{thing}")
#     return
#
# drink()
