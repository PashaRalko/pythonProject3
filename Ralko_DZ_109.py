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
