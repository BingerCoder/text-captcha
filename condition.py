# -*- coding: utf-8 -*-
from data import RandomData


class CalcException(Exception): pass


class Calc(object):
    """
    条件计算规则
    例如：
        求合
        取偶数
        取奇数
        取第三个值
        最大数
        最小数
    函数的返回结果
        问题，答案
    """
    Methods = [
        "sum",
        "get_even",
        "get_odd",
        "max",
        "min",
        "index_value",
    ]
    @staticmethod
    def sum(*args):
        ans = sum(map(int, args))
        return '%s的和' % '、'.join(map(str, args)), ans

    @staticmethod
    def get_even(*args):
        ans = ''.join([str(item) for item in map(int, args) if item % 2 == 0])
        if not ans:
            raise CalcException('No even number found in %s' % '、'.join(map(str, args)))
        return '%s里的偶数' % '、'.join(map(str, args)), ans

    @staticmethod
    def get_odd(*args):
        ans = ''.join([str(item) for item in map(int, args) if item % 2 != 0])
        if not ans:
            raise CalcException('No odd number found in %s' % '、'.join(map(str, args)))
        return '%s里的奇数' % '、'.join(map(str, args)), ans

    @staticmethod
    def max(*args):
        ans = max(map(int, args))
        return '%s里最大的数' % '、'.join(map(str, args)), ans

    @staticmethod
    def min(*args):
        ans = min(map(int, args))
        return '%s里最小的数' % '、'.join(map(str, args)), ans

    @staticmethod
    def index_value(index=None, *args):
        if index is None:
            index = RandomData.random_choice(range(len(args)))
        ans = args[index]
        return '%s里第%s个内容' % ('、'.join(map(str, args)), index + 1), ans


class ConditionConnection(object):
    """
    条件连接器，用于连接条件，组成问题
    例如：
        ... 和 ...
        ... 和 ... 的和
        ...
    """
    Single = 0
    Conbine = 1
    ConbineSum = 2
    Kinds = [
        (Single, lambda arg: arg, '%s'),  # 单条件
        (Conbine, lambda con1, con2: '%s%s' % (con1, con2), '%s和%s的连接'),  # 组合条件 "... 和 ..."
        (ConbineSum, lambda con1, con2: int(con1) + int(con2), '%s和%s的和'),  # 组合条件求和 "... 和 ... 的和"
    ]

    def __init__(self):
        pass

    @staticmethod
    def choice():
        return RandomData.random_choice(ConditionConnection.Kinds)


class Condition(object):
    """
    条件，用于生产一个简短的条件描述
    例如：
        第三个数
        所有的偶数
        第二个奇数
        今年的年份
        今年的月份
        北京奥运会的年份
    """
    Any = 0
    UseNative = 1
    UseData = 2

    def __init__(self, role):
        self.UseNative_Roles = [
            ("今年年份", RandomData.current_year()),
            ("本月月份", RandomData.current_month()),
            ("今天几号", RandomData.current_day()),
            ("北京奥运那年", "2008"),
        ]
        self.UseData_Roles = [
            Calc.sum(*[RandomData.get_int() for i in range(4)]),
            Calc.get_even(*[RandomData.get_int() for i in range(4)]),
            Calc.get_odd(*[RandomData.get_int() for i in range(4)]),
            Calc.max(*[RandomData.get_int() for i in range(4)]),
            Calc.min(*[RandomData.get_int() for i in range(4)]),
            Calc.index_value(None, *[RandomData.get_letter_digit() for i in range(4)]),
        ]
        if role == self.Any:
            role = RandomData.random_choice([self.UseData, self.UseNative])
        self.role = role

    def generate_condition(self):
        if self.role == Condition.UseNative:
            return RandomData.random_choice(self.UseNative_Roles)
        elif self.role == Condition.UseData:
            return RandomData.random_choice(self.UseData_Roles)
        else:
            raise Exception("role error")
