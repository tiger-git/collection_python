"""
基础模块：
random
time
re
"""

import random

['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType',
 '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
 '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools',
 '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate',
 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate',
 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle',
 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
a = '123'
b = [1, 2, 3]
# # TODO 可迭代对象里随机取值
# print(random.choice(a))
# print(random.choice(b))
# #TODO 两个书随机取一个
# print(random.randint(2,3))
# # TODO 0到1之间取小数，0<value<1
# print(random.random())
# # TODO　区间，步长，随机取值
# print(random.randrange(1, 22, 3))
# # TODO　可迭代对象随机取n个值
# print(random.sample(b,2))


# import time
# import datetime
#
# # print(time.ctime())
# # print(time.sleep(1))
# print(time.strptime('2020-1-1', "%Y-%m-%d"))
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# # print(datetime.datetime.now())
# print(datetime.datetime.now().strftime("%Y-%m-%d"))
# print(datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S"))
import re

aa = "abc123abd123"
result = re.search(r"^a.*3$", aa)
# print(dir(result))
# print(result.endpos)
# print(result.re)
# print(result.start())
# print(result.end())
# print(re.findall(r"1.*3$", aa))

# # TODO 贪婪模式匹配，通过 ? 区分
# print(re.findall(r"1.*3", aa))
# print(re.findall(r"1.*?3", aa))
# print(re.findall(r"1(.*)3", aa))
# print(re.findall(r"1(.*?)3", aa))

# # TODO 仅支持从第一个字符开始匹配
# print(re.match(r"a.*3", aa))
