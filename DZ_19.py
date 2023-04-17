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
            return True
        else:
            print("Помидор не созрел!")
            return False


tomat = Tomato(0)
print(tomat._state)
# tomat.grow()


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
        self.tomatoes = [Tomato(i) for i in range(count)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        list_of_True = list()
        for i in self.tomatoes:
            if i.is_ripe():
                list_of_True.append(True)
            else:
                list_of_True.append(False)

        if list_of_True.count(True) == len(self.tomatoes):
            print("Все помидоры спелые!")
            return True
        else:
            return False

    def give_away_all(self):
        if self.all_are_ripe() is True:
            print("Сбор урожая!")
            self.tomatoes = None
        else:
            print("Собирать урожай пока рано!")


tom = TomatoBush(5)
print(tom.tomatoes)
tom.grow_all()
tom.grow_all()
tom.grow_all()
tom.grow_all()
print(tom.all_are_ripe())
tom.give_away_all()

"""
Класс Gardener
1. Ȅоздайте класс Gardener
2. Ȅоздайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - 
передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является 
protected
3. Ȅоздайте метод work(), который заставляет садовника работать, что позволяет растению становиться 
более зрелым
4. Ȅоздайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. 
Если нет - метод печатает предупреждение.
5. Ȅоздайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
"""


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Опять работать...")
        self._plant.grow_all()

    def harvest(self):
        self._plant.give_away_all()

    @staticmethod
    def knowledge_base(gard):
        print(f"Имя садовника - {gard.name}")
        print(f"Кол-во томатов - {gard._plant.tomatoes}")
        print(f"Можно ли собирать урожай? {gard.harvest()}")


obj_ = TomatoBush(5)
gard = Gardener("Tom", obj_)
gard.work()
gard.harvest()
gard.knowledge_base(gard)
