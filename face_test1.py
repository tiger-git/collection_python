# 面试题1（阿里）

data = {
    "全球": [
        {"中国": ["北京", "杭州", "上海"]},
        {"美国": ["华盛顿", "洛杉矶", "纽约"]},
        {"英国": ["伦敦", "爱丁堡", "伯明翰"]}
    ]
}
# 有如下一组数据类型
example = [
    {"北京": 1, "杭州": 0, "上海": 1, "华盛顿": 0, "洛杉矶": 1, "纽约": 0, "伦敦": 0, "爱丁堡": 1, "伯明翰": 1},
    {"北京": 1, "杭州": 1, "上海": 0, "华盛顿": 1, "洛杉矶": 0, "纽约": 1, "伦敦": 1, "爱丁堡": 0, "伯明翰": 1},
    {"北京": 0, "杭州": 0, "上海": 1, "华盛顿": 0, "洛杉矶": 1, "纽约": 0, "伦敦": 0, "爱丁堡": 1, "伯明翰": 0},
    {"北京": 0, "杭州": 1, "上海": 1, "华盛顿": 1, "洛杉矶": 0, "纽约": 1, "伦敦": 0, "爱丁堡": 1, "伯明翰": 1},

    {"北京": 1, "杭州": 0, "上海": 0, "华盛顿": 1, "洛杉矶": 1, "纽约": 0, "伦敦": 1, "爱丁堡": 0, "伯明翰": 1},
    {"北京": 1, "杭州": 1, "上海": 1, "华盛顿": 1, "洛杉矶": 1, "纽约": 1, "伦敦": 0, "爱丁堡": 1, "伯明翰": 0},
    {"北京": 0, "杭州": 1, "上海": 1, "华盛顿": 0, "洛杉矶": 1, "纽约": 0, "伦敦": 1, "爱丁堡": 0, "伯明翰": 1},
    {"北京": 1, "杭州": 1, "上海": 1, "华盛顿": 1, "洛杉矶": 0, "纽约": 1, "伦敦": 1, "爱丁堡": 1, "伯明翰": 0}
]

# 已知data中
# 全球对应1级，
# 中国美国英国对应2级，
# "北京","杭州","上海","华盛顿","洛杉矶","纽约","伦敦","爱丁堡","伯明翰"对应3级。


# 1,当北京,杭州,上海　　其中有俩个为1的时候　　3级加一　　，当华盛顿,洛杉矶,纽约其中有俩个为1的时候3级加一，当伦敦,爱丁堡,伯明翰其中有俩个为1的时候3级加一。
# 2,当北京,杭州,上海　　连续俩次或者俩次以上其中有俩个为1的时候中国也为1　　(2级加一)　　　　，当华盛顿,洛杉矶,纽约连续俩次或者俩次以上其中有俩个为1的时候美国也为1(2级加一), 当伦敦,爱丁堡,伯明翰连续俩次或者俩次以上其中有俩个为1的时候英国也为1(2级加一)。
# 3,当中国，美国，英国连续俩次或者俩次以上其中有俩个为1的时候全球为1(1级加一)。
# 注:连续出现2次以上持续加一，例如连续两次加1，连续第三次则再加1
# 通过1,2,3，用代码求出example中1级，2级，3级1的次数。

# 答案
# 3级:17(正确)
# 2级:8（正确）
# 1级:3（未知）

[
    [1, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0]
]

#   中　美　英
[
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    [0, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1]
]


class Country(object):
    def __init__(self, data):
        self.first = 0
        self.second = 0
        self.third = 0
        self.country_city = tuple(data.values())[0]
        self.country = [tuple(x.keys())[0] for x in self.country_city]
        self.China = self.country_city[0]['中国']
        self.America = self.country_city[1]['美国']
        self.England = self.country_city[2]['英国']

    def sort_data(self, data):
        new_data = []
        for i, x in enumerate(data):
            value = []
            for c in self.country:
                citys = next(filter(lambda x: c in x.keys(), self.country_city)).values()
                citys = tuple(citys)[0]
                for city in citys:
                    value.append(
                        x[city]
                    )
            new_data.append(value)

    def get_third(self, data):
        self.third_data = [list(x.values()) for x in data]
        second_data = []
        for x in self.third_data:
            second_dict = dict()
            for i, c in enumerate(self.country):
                value = x[i * 3:(i + 1) * 3]
                if value.count(1) >= 2:
                    self.third += 1
                    second_dict[c] = 1
                else:
                    second_dict[c] = 0
            second_data.append(second_dict)
        self.second_data = [list(x.values()) for x in second_data]
        return

    def get_second(self):
        for x in range(len(self.country)):
            data = [s[x] for s in self.second_data]
            for d in range(len(data) - 1):
                if data[d] == data[d + 1] == 1:
                    self.second += 1
        return

    def get_first(self):
        data = self.second_data
        for x in range(len(self.second_data) - 1):
            if data[x].count(1) >= 2 and data[x + 1].count(1) >= 2:
                self.first += 1
        return

    def run(self, data):
        # print(data[0].values())
        # self.handle_data(data)
        self.get_third(data)
        self.get_second()
        self.get_first()
        # print(data[0].values())
        print(self.second_data)
        print(F"1级1的次数为{self.first}")
        print(F"2级1的次数为{self.second}")
        print(F"3级1的次数为{self.third}")
        return


# handle = Country(data)
# handle.run(example)

# TODO 面试题2(阿里)
# # 对一个整型数组a，和一个整数sum，找到数组a中两数之和等于sum的数对的下标，假设有且仅有一对满足，要求时间复杂度O(n)
# 如:
# a = [1, 5, 11, 2, 2, 7]
# sum = 4

# import copy
# a = [1, 5, 11, 2, 2, 7]
# sum = 18
# new_a = copy.deepcopy(a)
# new_a.sort()
# for x in new_a:
#     try:
#         other_index = new_a.index(sum-x)
#         value = new_a[other_index]
#         print(F"其中一个值为{x},原索引为{a.index(x)};另一个值为{value},原索引为{a.index(value)}")
#         break
#     except:
#         print(F"No {x}")
#         continue


# TODO 面试题3(华为)
# 如：连续正整数数组　l=[1,2,3,4]
# 连续正整数数组和　s=10,数组个数（长度） n为4，　0<s<100000,0<n<100000
# 求数组l
l = []


def face_3(s, n):
    s_n = (n - 1) * n / 2
    x = int((s - s_n) / n)
    if x < 0:
        return -1
    for i in range(n):
        l.append(x + i)
    return l

# print(face_3(3, 5))
# print(face_3(526, 6))
# print(face_3(10, 4))

