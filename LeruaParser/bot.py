from math import ceil
from time import sleep
from aiogram.dispatcher.filters.state import StatesGroup, State
import requests
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from environs import Env
from Parser import trees, girlyandy
from keyboard import keyboard, stopkeyboard

env = Env()
env.read_env()

bot = Bot(token=env.str("token"))
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Выберите функцию", reply_markup=keyboard)


@dp.message_handler(text=["🎅Гирлянды🎅"])
async def Girlyandy(message: types.Message):
    cards = girlyandy()
    for card in cards:
        result = f""
        for item in card:
            result += f"{item}\n"
        await message.answer(result, reply_markup=stopkeyboard)
        sleep(0.5)


@dp.message_handler(text=["🎄Ёлки🎄"])
async def Trees(message: types.Message):
    cards = trees()
    for card in cards:
        result = f""
        for item in card:
            result += f"{item}\n"
        await message.answer(result, reply_markup=stopkeyboard)
        sleep(0.5)


if __name__ == "__main__":
    executor.start_polling(dp)
