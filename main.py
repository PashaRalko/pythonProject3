class Human:
    default_name = "Name"
    default_age = 15

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, self.age, self.__house, self.__money)

    @staticmethod
    def default_info(self):
        print(self.default_age, self.default_name)

    def earn_money(self, count):
        self.__money += count
        return self.__money


ex = Human(13, "Hook")
ex.info()
Human.default_info(ex)
print(ex.earn_money(15))
 