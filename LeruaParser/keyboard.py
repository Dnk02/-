from aiogram import types


buttons = ["๐ะะปะบะธ๐", "๐ะะธัะปัะฝะดั๐"]

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*buttons)
