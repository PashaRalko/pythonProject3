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

