"""
Класс Tomato:
1. Ȅоздайте класс Tomato
2. Ȅоздайте статическое свойство states, которое будет содержать все стадии созревания помидора
3. Ȅоздайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1)
_index - передается параметром и 2) _state - принимает первое значение из словаря states
4. Ȅоздайте метод grow(), который будет переводить томат на следующую стадию созревания
5. Ȅоздайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)

"""


class Tomato:
    states = ["1 стадия", "2 стадия", "3 стадия", "4 стадия", "5 стадия"]

    def __init__(self, index, state=states[0]):
        self._index = index
        self._state = state


    def grow(self):
        if self._state != self.states[-1]:
            self._state = self.states[self.states.index(self._state) + 1]
            print(self._state)
        else:
            self.is_ripe()

    def is_ripe(self):
        if self._state == self.states[-1]:
            print("Помидор созрел!")
        else:
            print("Помидор не созрел!")


tomat = Tomato(0)
print(tomat._state)
#tomat.grow()


"""
1. Ȅоздайте класс TomatoBush
2. ȁпределите метод __init__(), который будет принимать в качестве параметра количество томатов и на его 
основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри 
динамического свойства tomatoes.
3. Ȅоздайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап 
созревания
4. Ȅоздайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
5. Ȅоздайте метод give_away_all(), который будет чистить список томатов после сбора урожая 
"""


class TomatoBush:

    def __init__(self, count):
        self.tomatoes = [f"obj_{i}" for i in range(count)]
        for i in self.tomatoes:
            print(f"сейчас объект {i}")
            i = Tomato(0)

    def grow_all(self):
        for i in self.tomatoes:
            print(f"сейчас объект {i}")
            #i.grow()


tom = TomatoBush(5)
print(tom.tomatoes)
tom.grow_all()

