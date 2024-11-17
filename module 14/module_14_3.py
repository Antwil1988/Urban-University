from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = 'YOUR_BOT_TOKEN'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Main keyboard
kb = InlineKeyboardMarkup(resize_keyboard=True)
btn1 = InlineKeyboardMarkup(text='Расчитать', callback_data='Расчитать')
btn2 = InlineKeyboardMarkup(text='Информация', callback_data='Информация')
btn3 = InlineKeyboardMarkup(text='Купить', callback_data='Купить')
kb.add(btn1, btn2, btn3)

# Inline keyboard
product_kb = InlineKeyboardMarkup(resize_keyboard=True)
product_kb1 = InlineKeyboardButton(text='Витамин B9', callback_data='product_buying')
product_kb2 = InlineKeyboardButton(text='Витамин D3', callback_data='product_buying')
product_kb3 = InlineKeyboardButton(text='Магний B6', callback_data='product_buying')
product_kb4 = InlineKeyboardButton(text='Цинк', callback_data='product_buying')
product_kb.add(product_kb1, product_kb2, product_kb3, product_kb4)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Выберите действие:', reply_markup=kb)


@dp.callback_query_handler(text='Информация')
async def info(call):
    await call.message.answer('Этот бот использует формулу разработанную группой американских врачей-диетологов под руководством докторов Миффлина и Сан Жеорадля расчета дневной нормы калорий для мужчин.')
    await call.answer()


@dp.callback_query_handler(text=['Расчитать'])
async def calc(call):
    await call.message.answer('Выберите действие:', reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calc_start'),
             InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')]
        ]))


@dp.callback_query_handler(text='formulas')
async def formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора: 10 * вес + 6.25 * рост - 5 * возраст - 161')
    await call.answer()


class User_State(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calc_start')
async def set_age(call):

    await call.message.answer('Введите свой возраст:')
    await User_State.age.set()


@dp.message_handler(state=User_State.age)
async def set_growth(message, state):

    await state.update_data(first=message.text)
    await message.answer('Введите свой рост:')
    await User_State.growth.set()


@dp.message_handler(state=User_State.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer('Введите свой вес:')
    await User_State.weight.set()


@dp.message_handler(state=User_State.weight)
async def send_calories(message, state):

    await state.update_data(third=message.text)
    data = await state.get_data()
    age = int(data['first'])
    growth = int(data['second'])
    weight = int(data['third'])
    if message.from_user.id % 2 == 0:
        calories = 10 * weight + 6.25 * growth - 5 * age - 161
    else:
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()

@dp.callback_query_handler(text='Купить')
async def get_buying_list(call):
    await call.message.answer_photo(photo='https://iimg.su/i/RxN9U', caption='Название: Витамин B9 | Описание: описание 1 | Цена: 100 ')
    await call.message.answer_photo(photo='https://iimg.su/i/p0Z4b', caption='Название: Витамин D3 | Описание: описание 2 | Цена: 200 ')
    await call.message.answer_photo(photo='https://iimg.su/i/R6cdY', caption='Название: Магний B6 | Описание: описание 3 | Цена: 300 ')
    await call.message.answer_photo(photo='https://iimg.su/i/nVcrs', caption='Название: Цинк | Описание: описание 4 | Цена: 400 ')
    await call.message.answer('Выберите продукт для покупки: ', reply_markup=product_kb)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

