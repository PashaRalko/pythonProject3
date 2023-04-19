from datetime import datetime


def create_list():
    start = datetime.now()
    list_ = []
    for _ in range(10 ** 5):
        if _ % 2 == 0:
            list_.append(_)
    print(datetime.now() - start)
    return list_


def create_list_gen():
    start = datetime.now()
    list_ = [i for i in range(10 ** 5) if i % 2 == 0]
    print(datetime.now() - start)
    return list_


ex1 = create_list()
ex2 = create_list_gen()
