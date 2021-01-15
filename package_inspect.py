# 参考：
# https://www.cnblogs.com/yaohong/p/8874154.html

# TODO package 1
# import inspect


# class Apple(object):
#     def __init__(self, name='ipad'):
#         self.name = name
#
#     @staticmethod
#     def hello():
#         print('hello')
#         pass
#
#     @classmethod
#     def world(cls):
#         return cls()
#
#     def myprint(self, obj='something'):
#         self.hello()
#         print(F"this is:{obj}")
#         # 堆栈解析
#         info = inspect.stack()
#         print(len(info), info)
#         data = info[1]
#         print(len(data), type(data), *data, sep='\n')
#         return

# # TODO 获取源码
# print(inspect.getsource(Apple.myprint))
# print(inspect.getsourcelines(Apple.myprint))
# ...

# # TODO 类，模块，函数等类型判断
# print(inspect.isclass(Apple))
# print(inspect.ismodule(inspect))
# print(inspect.ismethod(Apple.world))
# print(inspect.isfunction(Apple.myprint))
# ...

# # TODO 获取类或者函数的参数信息
# print(inspect.getargspec(Apple))
# print(inspect.getargspec(Apple.hello))
# print(inspect.getargspec(Apple.world))
# print(inspect.getargspec(Apple.myprint))

# # TODO 解析堆栈（程序执行过程信息）
# a = Apple("Ipad")
# a.myprint(a.name)
# # inspect.stack()  # [frame][frame对象，代码文件绝对路径，代码行，函数名，代码，***]
