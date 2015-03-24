# -*- coding: utf-8 -*-
from condition import ConditionConnection, Condition, CalcException


def get_captcha():
    condition_connections = ConditionConnection.choice()
    if condition_connections[0] == ConditionConnection.Single:  # 单个条件
        cond = Condition(Condition.Any).generate_condition()
        return condition_connections[2] % cond[0], condition_connections[1](cond[1])
    elif condition_connections[0] == ConditionConnection.Conbine:   # 组合条件
        cond1 = Condition(Condition.Any).generate_condition()
        cond2 = Condition(Condition.Any).generate_condition()
        return condition_connections[2] % (cond1[0], cond2[0]), condition_connections[1](cond1[1], cond2[1])
    elif condition_connections[0] == ConditionConnection.ConbineSum:    # 组合求合
        cond1 = Condition(Condition.UseData).generate_condition()
        cond2 = Condition(Condition.UseData).generate_condition()
        return condition_connections[2] % (cond1[0], cond2[0]), condition_connections[1](cond1[1], cond2[1])


if __name__ == "__main__":
    while True:
        try:
            question, answer = get_captcha()
            print question.decode("utf-8")
            print answer
            break
        except CalcException:
            pass
