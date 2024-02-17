import random
from random import choice


class Count:
    def __init__(self):
        __num1 = num1
        __num2 = num2

    def __counting(self, __num1, __num2):
        operation = ["+", "-", "*", "/"]
        a_choice = choice(operation)
        if operation == "+":
            return __num1 + __num2
        if operation == "-":
            return __num1 - __num2
        if operation == "*":
            return __num1 * __num2
        if operation == "/":
            return __num1 / __num2
        def result(self):
            return self.__counting()



num1 = 25
num2 = 50
rand = Count(num1, num2)
print(rand.result())

