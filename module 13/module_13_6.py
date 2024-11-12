from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = 'Your_Bot_Token'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup(resize_keyboard=True)
btn1 = InlineKeyboardMarkup(text='Расчитать', callback_data='Расчитать')
btn2 = InlineKeyboardMarkup(text='Информация', callback_data='Информация')
kb.add(btn1, btn2)


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

