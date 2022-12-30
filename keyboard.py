from aiogram import types


buttons = ["🎄Ёлки🎄", "🎅Гирлянды🎅"]
stopbutton = "⛔STOP⛔"

inlinebuttons = [types.InlineKeyboardButton(text="Быстрый вывод всех товаров", callback_data="быстрый вывод"), types.InlineKeyboardButton(text="Показать половину", callback_data="половина"), types.InlineKeyboardButton(text="Обычный вывод", callback_data="обычный режим")]

stopkeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
inlinekeyboard = types.InlineKeyboardMarkup(row_width=1)

inlinekeyboard.add(*inlinebuttons)
keyboard.add(*buttons)
stopkeyboard.add(stopbutton)