from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основа для кнопок

info = types.KeyboardButton("Информация")
stats = types.KeyboardButton("Список литературы")

start.add(stats, info)

# Ин-лайн кнопки
stats = InlineKeyboardMarkup()
stats.add(InlineKeyboardButton("Yes", callback_data="show_statistic"))
stats.add(InlineKeyboardButton("No", callback_data="cansel"))