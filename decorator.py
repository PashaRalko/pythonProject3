# функция возвращает элементы из списка кратные 3, а декоратор выводит элементы не кратные 3
def decorator(func):
    print("Вызвался декоратор!")

    def wrapper(args):
        new_list = list()
        for i in args:
            for _ in i:
                if _ % 3 != 0:
                    new_list.append(_)  # записываем элементы не кратные 3
        print(new_list)
        return func(args)

    return wrapper


@decorator
def func(list_):
    new_list = list()
    for _ in list_:
        for i in _:
            if i % 3 == 0:
                new_list.append(i)  # записываем элементы кратные 3
    return new_list


list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(func(list_1))

"""
Напишите декоратор debug, который при каждом вызове
декорируемой функции выводит её имя (вместе со всеми
передаваемыми аргументами), а затем — какое значение
она возвращает. После этого выводится результат её
выполнения
"""


def debug(f):
    def wrapper(*args):
        print(f"Название функции - {f.__name__}{args}\nАргументы в ней - {args}\nВозвращает - {f(*args)}")
        return f(*args)

    return wrapper


@debug
def func(*args):
    return sum(args)


print(func(1, 2, 3))
print(func(2, 2, 3))
print(func(3, 2, 3))
