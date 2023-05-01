import random

"""
Реализуйте итератор колоды карт (52 штуки) CardDeck.
Каждая карта представлена в виде строки типа «2 Пик».
При вызове функции next() будет представлена
следующая карта. По окончании перебора всех
элементов возникнет ошибка StopIteration.
"""


class CardDeck:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index + 1 != len(self.lst):
            self.index += 1
            self.str_2 = self.lst[self.index]
            return self.str_2
        else:
            raise StopIteration


card_suit = ["Пики", "Червы", "Бубны", "Крести"]
card_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

cards = list()

for i in card_suit:
    for x in card_value:
        cards.append(f"{x} {i}")

example = CardDeck(cards)

for i in example:
    print(i)

# Доп. задачи
"""
1. Напишите генератор, который на вход получает список чисел
 и возвращает только те числа, которые делятся на 3 без остатка.
"""


def generator(list_):
    for i in list_:
        if i % 3 == 0:
            yield i


list_ = [i for i in range(1, 20)]

list_1 = [i for i in generator(list_)]
print(list_1)

"""
2. Напишите итератор, который на вход получает строку и возвращает каждый второй символ этой строки.
"""


class Example:
    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index != len(self.list_):
            str_ = self.list_[self.index]
            self.index += 2
            return str_
        else:
            raise StopIteration


ex = Example(["1", "2", "3", "4", "5", "6", "7", "8"])

for i in ex:
    print(i)

"""
3. Напишите генератор, который на вход получает два списка чисел
 и возвращает только те числа, которые есть в обоих списках.
"""


def generator(lst1, lst2):
    for i in lst1:
        if i in lst2:
            yield i


list_1 = [random.randint(0, 10) for i in range(5)]
list_2 = [random.randint(0, 10) for i in range(5)]

list_3 = [i for i in generator(list_2, list_1)]

"""
4. Напишите генератор, который на вход получает список строк
 и возвращает только те строки, которые содержат букву "a".
"""


def generator(lst):
    for _ in lst:
        if "a" in _ or "а" in _:
            yield _


list_ = ["12a3", "456", "78a9", "110", "aaaa", "русская а"]

list_2 = [i for i in generator(list_)]
print(list_2)

"""
5. Напишите итератор, который на вход получает список чисел и возвращает каждый третий элемент этого списка.
"""


class Example:
    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index + 1 < len(self.list_):
            str_ = self.list_[self.index]
            self.index += 3
            return str_
        else:
            raise StopIteration


ex = Example(["1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "123"])

for i in ex:
    print(i)
