"""
Дополнительная задача:
1. Создать класс "Сотрудник" +
2. Определить атрибуты класса: имя, фамилия, должность, зарплата +
3. Определить конструктор класса для инициализации атрибутов +
4. Реализовать методы для изменения и получения значений каждого атрибута +
5. Реализовать метод для вывода информации о сотруднике на экран +
6. Создать несколько объектов класса "Сотрудник" +
7. Продемонстрировать работу методов на созданных объектах +

Расширение задачи:
8. Добавить в класс "Сотрудник" метод для изменения зарплаты на заданное значение +
9. Добавить в класс "Сотрудник" метод для увеличения зарплаты на заданное процентное значение +
10. Добавить в класс "Сотрудник" метод для сравнения зарплаты
текущего объекта с зарплатой другого объекта класса "Сотрудник" +
11. Продемонстрировать работу новых методов на созданных объектах. +
"""
import csv


class Employee:

    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.new_name = None
        self.full_name = None

    def get_name(self):
        print(f"Имя сотрудника: {self.name} {self.surname}")
        choice = input("Хотите ли вы поменять имя сотрудника? (+/-) ")
        self.full_name = self.name + "" + self.surname
        if choice == "-":
            return self.full_name
        elif choice == "+":
            self.new_name = input("Введите новое имя и фамилию (name surname) ")
            self.name, self.surname = self.new_name[0], self.new_name[1]
            self.full_name = self.name + "" + self.surname
            print(f"Теперь сотрудника зовут {self.full_name}")
            return self.full_name

    def get_position(self):
        print(f"Должность сотрудника {self.position}")
        choice = input("Хотите ли вы поменять должность сотрудника? (+/-) ")

        if choice == "-":
            return self.position
        elif choice == "+":
            self.position = input("Введите новую должность сотрудника ")
            print(f"Теперь должность сотрудника {self.position}")
            return self.position

    def get_salary(self):
        print(f"Зарплата сотрудника {self.salary}")
        choice = input("Хотите ли вы поменять зарплату сотрудника? (+/-) ")

        if choice == "-":
            return self.salary
        elif choice == "+":
            self.salary = input("Введите новую зарплату сотрудника ")
            print(f"Теперь зарплата сотрудника {self.salary}")
            return self.salary

    def get_info(self):
        print(
            f"Имя сотрудника {self.get_name()}\n"
            f"Должность сотрудника {self.get_position()}\n"
            f"Зарплата сотрудника {self.get_salary()}")

    def change_to(self, value):
        self.salary += value
        print(self.salary)
        return self.salary

    def change_percent(self, percent):
        self.salary += (self.salary / percent) * 100
        print(self.salary)
        return self.salary

    def compare_salary(self, obj):
        if self.salary > obj.salary:
            print(f"Зарплата у {self.name} больше")
        else:
            print(f"Зарплата у {obj.name} больше")

    def write_to_csv(self, value):
        with open("change_salary.csv", "a") as file_csv:
            change_salary_list = [f"Сотрудник", "ЗП была", 'изменение', "Стало"]
            writer = csv.DictWriter(file_csv, fieldnames=change_salary_list)

            writer.writeheader()
            writer.writerow(
                {'Сотрудник': self.name, 'ЗП была': self.salary, 'изменение': value, "Стало": self.change_to(value)})


emp_1 = Employee("Ivan", "Ivanov", "Manager", 1300)
emp_2 = Employee("Anna", "Ivanova", "Director", 9020)

emp_1.get_info()
emp_2.get_info()
emp_2.compare_salary(emp_2)
emp_1.change_percent(10)

emp_2.change_to(20)

emp_1.write_to_csv(20)

"""
Два метода в классе, один принимает в себя либо строку, либо число.
Если я передаю строку, то смотрим:
если произведение гласных и согласных букв
меньше или равно длине слова, выводить все гласные,
иначе согласные; если число то, произведение суммы чётных цифр
на длину числа. Длину строки и числа искать во втором методе.
"""


class Example:
    def init(self, var):
        self.var = var

    def str_or_num(self):
        if isinstance(self.var, str):
            print("Это строка!")
            number_of_vowels = 0
            number_of_consonants = 0
            list_of_vowels = list()
            list_of_consonants = list()
            for iter_ in self.var.lower():
                if iter_ in "аоиыуэ" or iter_ in "aeiouy":
                    number_of_vowels += 1
                    list_of_vowels.append(iter_)
                else:
                    number_of_consonants += 1
                    list_of_consonants.append(iter_)
            if number_of_vowels * number_of_consonants <= self.var_len():
                print(list_of_vowels)
            else:
                print(list_of_consonants)
        elif isinstance(self.var, int):
            print("Это число!")
            list_of_even = list()
            for iter_ in str(self.var):
                if int(iter_) % 2 == 0:
                    list_of_even.append(int(iter_))
            print(sum(list_of_even) * self.var_len())

    def var_len(self):
        return len(str(self.var))


str_1 = Example("Строка")
str_1.str_or_num()

num_1 = Example(452)
num_1.str_or_num()
