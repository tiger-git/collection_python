# 面试题

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

[
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1]
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

    def add_1(self, obj: int):
        self.first += obj
        return

    def add_2(self, obj: int):
        self.second += obj

    def add_3(self, obj: int):
        self.third += obj

    def add_data(self, data_dict: dict, country: str):
        if country == '中国':
            key = self.China
        elif country == '美国':
            key = self.America
        elif country == '英国':
            key = self.England
        else:
            print('error')
            return
        for k in key:
            data_dict[k] += 1
        return data_dict

    def handle_data(self, data: list):
        for index, i in enumerate(data):
            self.handle_dict(data, i, index)
        return

    def handle_dict(self, data: list, obj: dict, index):
        key = list(obj.keys())
        value = list(obj.values())
        China = value[:3]
        America = value[3:6]
        England = value[6:9]
        # reback = False
        for c in self.earth_country:
            if c == '中国' and China.count(1) == 2:
                self.add_3(1)
                # self.add_3(China.count(1))
                # reback = True
                # break
            if c == '美国' and America.count(1) == 2:
                self.add_3(1)
                # self.add_3(America.count(1))
                # reback = True
                # break
            if c == '英国' and England.count(1) == 2:
                self.add_3(1)
                # self.add_3(England.count(1))
                # reback = True
                # break
        # if reback:
        # print(index,c)
        # data[index] = self.add_data(obj, c)
        # self.handle_data(data)
        return

    def get_third(self, data):
        self.third_data = [list(x.values()) for x in data]
        second_data = []
        for x in self.third_data:
            second_dict = dict()
            for i, c in enumerate(self.country):
                value = x[i * 3:(i + 1) * 3]
                if value.count(1) == 2:
                    self.add_3(1)
                    second_dict[c] = 1
                else:
                    second_dict[c] = 0
            second_data.append(second_dict)
        self.second_data = [list(x.values()) for x in second_data]
        return

    def get_second(self):
        second = 0
        for x in range(3):
            data = [s[x] for s in self.second_data]
            second += data.count(1) - 1
        self.second = second
        return

    def get_first(self):
        data = list(map(lambda x: x.count(1), self.second_data))
        self.first = data.count(2)
        return

    def run(self, data):
        # print(data[0].values())
        # self.handle_data(data)
        self.get_third(data)
        self.get_second()
        self.get_first()
        # print(data[0].values())
        print(self.second_data)
        print(self.first)
        print(self.second)
        print(self.third)
        return


handle = Country(data)
handle.run(example)
