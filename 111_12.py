from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7616859155:AAEORIw8E63b3WJy_WPk5ucXgGhmfqQ6Ues"
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

# @dp.message_handler(text= ['Urban', 'ff'])
# async def urban_message(message):
#     print("Urban messang")
#
# @dp.message_handler(commands= ['start'])
# async def start_message(message):
#     print("start message")
#
# @dp.message_handler()
# async def all_message(message):
#     print("Мы получили сообщение!")


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)