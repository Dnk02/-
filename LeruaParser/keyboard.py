from aiogram import types


buttons = ["🎄Ёлки🎄", "🎅Гирлянды🎅"]

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*buttons)
