class Calculator:
    def __init__(self):
        self.x = int(input("Введите число х: "))
        self.y = int(input("Введите число y: "))
        self.oper = input("Какая операция: ")

    def sum_(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def multy(self):
        return self.x * self.y

    def div(self):
        try:
            rez = self.x / self.y
            return rez
        except ZeroDivisionError:
            print("Деление на 0")
            main()


def main():
    calc_ = Calculator()

    if calc_.oper == "+":
        print(calc_.sum_())
    elif calc_.oper == "-":
        print(calc_.minus())
    elif calc_.oper == "*":
        print(calc_.multy())
    elif calc_.oper == "/":
        print(calc_.div())
    else:
        print("что-то пошло не так...")
        main()


if __name__ == "__main__":
    main()
