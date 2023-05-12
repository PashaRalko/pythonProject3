types_list = [
    1,
    "строка",
    [1, 2, 3],
    {1, 2, 3},
    1.1,
    True,
    (1, 2, 3),
    frozenset({1, 2, 3}),
    {"key": "value"},
    range(1, 10)
]

for i in types_list:
    print(f"Тип данных: {type(i)},"
          f"наличие __iter__: {'__iter__' in i.__dir__()},"
          f"наличие __getitem__: {'__getitem__' in i.__dir__()}")


class Xrange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        self.value = self.start - self.step
        print(f"изначальное значение value в iter: {self.value}")
        print("был вызван метод iter")
        return self

    def __next__(self):
        if self.value + self.step <= self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


example = Xrange(10, 12, 1)

for i in example:
    print(i)