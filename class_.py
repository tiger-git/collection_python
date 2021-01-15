"""
类的理解及使用
"""


class Human(object):
    """
    __doc__
    类的文档字符串
    """
    chinese = '人类'  # 类变量（类属性）
    language = 'Python'

    @property
    def sex(self):
        return self._sex

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        try:
            age = int(value)
            if age > 100 or age < 0:
                raise ValueError
            self._age = age
        except ValueError as e:
            print(F'年龄值错误，{e}')
        print(F"{self.name}当前年龄为{self.age}")

    def __init__(self, name, age, sex):  # 归属实例方法
        self._sex = sex
        self._name = name
        self._age = age
        self.eat_thing = ''

    @classmethod
    def get_split(cls, obj: str):
        data = obj.split('-')
        return cls(*data)

    @staticmethod
    def get_time():
        import datetime
        data = datetime.datetime.now()
        data = data.strftime("%Y年%m月%d日")
        print(F"今天是{data}")
        return data

    def eat(self, thing='', default='东西'):
        """
        实例方法
        :param thing:
        :return:
        """
        if thing:
            self.eat_thing = thing  # 实例属性（实例变量）
        elif not self.eat_thing:
            self.eat_thing = default
        data = F"{self.name}在吃{self.eat_thing}？"

        print(data)
        return data

    def introduce(self):
        print(f"当前是用{Human.language}写的例子")  # 类变量调用


class Boy(Human):
    """
    我是学生
    """
    tiger = 18

    def __init__(self, age, name='某某某'):
        Human.__init__(self, name, age, '男')
        self._key = '123456'

    @property
    def key(self):
        return self._key

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = str(value)

    @staticmethod
    def print_age(value=1):
        print(value)
        return

    def say_value(self):
        print(self.name)
        return

    def eat(self, thing='', default='东西'):  # 多肽,覆盖父类方法
        """
        实例方法重构
        :param thing:
        :param default:
        :return:
        """
        # data = super(Boy, self).eat(thing, default)  # 继承并调用父类方法1
        data = Human.eat(self, thing, default)  # 继承并调用父类方法2(推荐)
        data = data.replace('？', '。')
        print("重构的方法", data)
        return data


h = Human("Jenny", 18, '女')  # 实例化一个对象
# h.eat('汉堡')  # 实例方法调用1(对象，常规)
# Human.eat(h, '汉堡')  # 实例方法调用2（类名调用）
# h.__init__('John', 20, '男')  # 对象调用实例方法（重新初始化）
# h.eat('汉堡')
# TODO 类的静态方法与类方法
# h.get_time()
# h.eat()
# h = h.get_split('tiger-20-男')  # 类方法，重新初始化，返回一个实例对象
# h.eat()

# TODO 实例变量与类变量
# h1 = Human("Jenny", 18, '女')
# h2 = Human('John', 20, '男')
# h1.eat('冰淇淋')
# print(h1.eat_thing)

# h2.eat('汉堡')
# print(h2.eat_thing)
# h1.eat_thing = '炸鸡'  # 实例变量跟随实例对象
# h1.eat()
# h2.eat()
# h.introduce()
# h1.introduce()
# h2.introduce()
# # h.language = 'java'#对象修改类变量（仅修改局部变量）
# Human.language = 'java'  # 类修改类变量（不可取，将修改全局类变量）
# h.introduce()
# h1.introduce()
# h2.introduce()
# TODO 类的继承，多肽
b = Boy(18, '小明')
# Human.eat(b)  # 对象调用父类方法
# b.eat()  # 对象调用子类方法（覆盖或重写父类的方法）
# b.introduce()  # 继承父类的方法
# print(h.age)
# h.age = 22
# print(b.age)
# b.age = 101
# print(b.__doc__)  # 文档字符串，介绍
print(b.__dict__)  # 对象，属性值
print(dir(b))
import inspect
# print(inspect.getsource(Boy))#获取源码
# print(inspect.getsource(b.eat))
# print(inspect.getargspec(b.eat))
