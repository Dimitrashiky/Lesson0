from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import FSInputFile


api = ""
bot = Bot(token=api)
dp = Dispatcher(storage= MemoryStorage())
keyboard = ReplyKeyboardMarkup(keyboard= [[KeyboardButton(text= "Рассчитать"), KeyboardButton(text= "Информация")],
                                          [KeyboardButton(text= "Купить")]], resize_keyboard= True)

inline_keyboard = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data= "calories")],
                                                          [InlineKeyboardButton(text= "Формула расчета", callback_data= "formulas")]] )

inline_keyboard_2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Product1", callback_data="product_buying"),
                                                           InlineKeyboardButton(text="Product2", callback_data="product_buying"),
                                                           InlineKeyboardButton(text="Product3", callback_data="product_buying"),
                                                           InlineKeyboardButton(text="Product4", callback_data="product_buying")]])
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(CommandStart())
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup= keyboard)


@dp.message(F.text == "Рассчитать")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup= inline_keyboard)

@dp.callback_query(F.data == "formulas")
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")



@dp.callback_query(F.data == "calories")
async def set_age(call, state: FSMContext):
    await state.set_state(UserState.age)
    await call.message.answer("Введите свой возраст:")

@dp.message(UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(age= message.text)
    await state.set_state(UserState.growth)
    await message.answer("Введите свой рост:")

@dp.message(UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer("Введите свой вес:")

@dp.message(UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) + 5
    await message.answer(f"Ваша норма калорий {calories}")
    await state.clear()

@dp.message(F.text == "Купить")
async def get_buying_list(message):
    for number in range(1, 5):
        photo = FSInputFile(f"images/i{number}.jpg", )
        await message.answer(f"Название: Product{number} | Описание: описание {number} | Цена: {number * 100}")
        await message.answer_photo(photo)
    await message.answer("Выберите продукт для покупки:", reply_markup= inline_keyboard_2)


@dp.callback_query(F.data == "product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')




async def main():
    await dp.start_polling(bot)




#Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5
#Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161






if __name__ == "__main__":
    asyncio.run(main())
