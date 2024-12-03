from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

api = "7867274709:AAHYgWkZ4GZaYmksMvwwCv4U0iCSoiPnWmw"
bot = Bot(token=api)
dp = Dispatcher(storage= MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message(F.text == "Calories")
async def set_age(message, state: FSMContext):
    await state.set_state(UserState.age)
    await message.answer("Введите свой возраст:")

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


@dp.message(CommandStart())
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')




@dp.message()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')




async def main():
    await dp.start_polling(bot)




#Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5
#Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161






if __name__ == "__main__":
    asyncio.run(main())