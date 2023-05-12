import random
from datetime import datetime
import time
import asyncio


async def f1(n1, n2):
    print(f'Запуск функции: f1')
    print(f'Выполнение текущего кода 1: {sum(x for x in range(random.randint(n1, n2)))}')
    print('f1 засыпает...')
    await asyncio.sleep(3)
    print('f1 очнулась и завершена')


async def f2(n1, n2):
    print(f'Запуск функции: f2')
    print(f'Выполнение текущего кода 2: {sum(random.randint(n1, n2) for x in range(10))}')
    print('f2 засыпает...')
    await asyncio.sleep(3)  # засыпаем на 3 секунды
    print('f2 очнулась и завершена')  # выводим сообщение

loop = asyncio.new_event_loop()
task1 = loop.create_task(f1(5, 10))
task2 = loop.create_task(f2(2, 8))

print(time.strftime("%X"))
loop.run_until_complete(asyncio.wait([task1, task2]))
print(time.strftime("%X"))
