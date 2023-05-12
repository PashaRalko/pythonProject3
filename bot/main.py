from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
import asyncio
import aiogram.dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config  # импортируем файл config
import keyboard  # импортируем файл keyboard

import logging  # модуль для вывода информации

storage = MemoryStorage()  # FSM
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)  # хранилище состояний в оперативной памяти

logging.basicConfig(
    # указываем название с логами
    filename='log.txt',
    # указываем уровень логирования
    level=logging.INFO,
    # указываем формат сохранения логов
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s')


@dp.message_handler(Command("start"), state=None)  # задаем название команды start
async def welcome(message):
    joinedFile = open("user.txt", "r")
    joinedUsers = set()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("user.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)

    await bot.send_message(message.chat.id,
                           f"HI, *{message.from_user.first_name} {message.from_user.last_name},* bot works",
                           reply_markup=keyboard.start,
                           parse_mode="Markdown")
    # после проверки и записи выводим сообщение с именем пользователя и отображения кнопки


@dp.message_handler(content_types=['text'])
async def get_message_literature(message):
    if message.text == "Список литературы":
        await bot.send_message(message.chat.id,
                               text="1) Простой Python. Современный стиль программирования. 2-е изд. Любанович Б.\n"
                                    "2) Python 3 и PyQt 6. Разработка приложений. Прохоренок Н. А.\n"
                                    "3) Машинное обучение с использованием Python. Сборник рецептов Элбон Крис")
    elif message.text == "Информация":
        await bot.send_message(message.chat.id, text="Информация\nБот для обучения")

    else:
        await bot.send_message(message.chat.id, text="Введено что-то не то!")


if __name__ == "__main__":  # чтобы бот работал
    print("Бот запущен!")
    executor.start_polling(dp)
