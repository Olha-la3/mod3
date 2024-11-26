from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
import asyncio


api = "7616859155:AAEORIw8E63b3WJy_WPk5ucXgGhmfqQ6Ues"
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

    # kb = ReplyKeyboardMarkup()
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
kb.add(button)  # метод в который передаём кнопку Существует несколько методов добавления кнопок в клавиатуру:
    # - Метод «add» - посторочно ;
    # - Метод «row», который позволяет добавить несколько кнопок в один ряд
    # kb.insert - добавляет кнопку в последний ряд
button2 = KeyboardButton(text='Информация')
kb.insert(button2)
button3 = KeyboardButton(text='Купить')
kb.add(button3)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)  # показывает клавиатуру

@dp.message_handler(text='Рассчитать')
async def inform(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()  # Установка состояния для возраста

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.answer('Введите свой рост:')  # Запрашиваем рост
    await UserState.growth.set()  # Устанавливаем состояние для роста

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.answer('Введите свой вес:')  # Запрашиваем вес
    await UserState.weight.set()  # Устанавливаем состояние для веса

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес

    data = await state.get_data()
    age = int(data.get('age', 0))
    growth = int(data.get('growth', 0))
    weight = int(data.get('weight', 0))

    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал')
    await state.finish()  # Завершаем состояние

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products_info = ""

    products = [
        ("Омега 3 концентрации 90% 1300мг", "Полезная добавка для сердца и сосудов", 1300),
        ("Магний хелат бисглицинат + B6", "Поддержка нервной системы и сердечно-сосудистой системы", 800),
        ("Витамин Д3 + К2 (D3 К2) 5000 МЕ", "Укрепление костей и зубов", 500),
        ("Коллаген морской 1-3 типа + витамин С + Биотин", "Для здоровья кожи и суставов", 1200),
    ]

    inline_keyboard = InlineKeyboardMarkup()

     for i in range(1, 5):
         product_name = f"Product{i}"
         product_desc = f"Описание {i}"
         product_price = i * 100

         products_info += f'Название: {product_name} | Описание: {product_desc} | Цена: {product_price}\n'

         # Добавляем кнопку для каждого продукта
         inline_keyboard.add(InlineKeyboardButton(text=product_name, callback_data="product_buying"))
    #
    # for product_name, product_desc, product_price in products:
    #     products_info += (
    #         f'Название: {product_name}\n'
    #         f'Описание: {product_desc}\n'
    #         f'Цена: {product_price} руб.\n\n'
    #     )
    #     # Добавляем кнопку для каждого продукта
    #     inline_keyboard.add(InlineKeyboardButton(text=product_name, callback_data=f"buy_{product_name}"))
    #
    # await message.answer(products_info)
    # await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)
   #  products = [
   #      ("Омега 3 концентрации 90% 1300мг", "Полезная добавка для сердца и сосудов", 1300),
   #      ("Магний хелат бисглицинат + B6", "Поддержка нервной системы и сердечно-сосудистой системы", 800),
   #      ("Витамин Д3 + К2 (D3 К2) 5000 МЕ", "Укрепление костей и зубов", 500),
   #      ("Коллаген морской 1-3 типа + витамин С + Биотин", "Для здоровья кожи и суставов", 1200),
   #  ]
   #
   # #                   "Омега 3 концентрации 90% 1300мг"),
   # # "Магний хелат бисглицинат+ B6", "Витамин Д3 + К2 (D3 К2) 5000 МЕ",
   # #  "Коллаген морской 1-3 типа + витамин С + Биотин"
   #  inline_keyboard = InlineKeyboardMarkup()  # Создаем inline-клавиатуру
   #
   #  for i in range(1, 5):
   #      product_name = f"Product{i}"
   #      product_desc = f"Описание {i}"
   #      product_price = i * 100
   #
   #      products_info += f'Название: {product_name} | Описание: {product_desc} | Цена: {product_price}\n'
   #
   #      # Добавляем кнопку для каждого продукта
   #      inline_keyboard.add(InlineKeyboardButton(text=product_name, callback_data="product_buying"))
   #
   #      # Здесь вы можете добавить отправку изображения продукта, если они у вас есть
   #  # await bot.send_photo(chat_id=message.chat.id, photo=open(f'path_to_image_{i}.jpg', 'rb'))
   #  # await bot.send_foto(chat_id=message.chat.id, photo=photo)
   #
   #  await message.answer(products_info)
   #  await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()  # Обязательный вызов, чтобы избежать таймаутов
    await call.message.reply_text("Вы успешно приобрели продукт!")


# # Функция для старта бота
# def start(update: Update, context: CallbackContext) -> None:
#     main_keyboard = [[KeyboardButton("Купить")]]
#     reply_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)
#     update.message.reply_text("Добро пожаловать! Выберите действие:", reply_markup=reply_markup)
#
#
# # Функция для получения списка товаров
# def get_buying_list(update: Update, context: CallbackContext) -> None:
#     products_info = ""
#     product_images = []  # Здесь вы можете хранить пути к изображениям
#
#     for i in range(1, 5):
#         product_name = f"Product{i}"
#         product_desc = f"Описание {i}"
#         product_price = i * 100
#
#         # Составляем текст для каждого продукта
#         products_info += f'Название: {product_name} | Описание: {product_desc} | Цена: {product_price}\n'
#         # Здесь добавьте код для загрузки изображений (например, с помощью context.bot.send_photo)
#         product_images.append(f"image_path_{i}.jpg")  # Пример изображений
#
#     # Отправляем список продуктов
#     update.message.reply_text(products_info)
#
#     # Создаем inline-клавиатуру
#     inline_keyboard = [
#         [InlineKeyboardButton("Product1", callback_data="product_buying")],
#         [InlineKeyboardButton("Product2", callback_data="product_buying")],
#         [InlineKeyboardButton("Product3", callback_data="product_buying")],
#         [InlineKeyboardButton("Product4", callback_data="product_buying")]
#     ]
#     reply_markup = InlineKeyboardMarkup(inline_keyboard)
#     update.message.reply_text("Выберите продукт для покупки:", reply_markup=reply_markup)
#
#
# # Функция для обработки нажатия кнопки "Купить"
# def handle_buy_command(update: Update, context: CallbackContext) -> None:
#     get_buying_list(update, context)
#
#
# # Функция для обработки коллбэков
# def send_confirm_message(call: Update.CallbackQuery) -> None:
#     call.answer()  # Обязательный вызов, чтобы избежать таймаутов
#     call.message.reply_text("Вы успешно приобрели продукт!")
#
#
# def main() -> None:
#     # Замените 'YOUR_TOKEN' на токен вашего бота
#     updater = Updater("YOUR_TOKEN")
#
#     # Получаем диспетчер для регистрации обработчиков
#     dp = updater.dispatcher
#
#     # Регистрация обработчиков
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_buy_command))
#     dp.add_handler(CallbackQueryHandler(send_confirm_message, pattern="product_buying"))

    # Запускаем бота
#     updater.start_polling()
#     updater.idle()
#
#
# if __name__ == '__main__':
#     main()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)