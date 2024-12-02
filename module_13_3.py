from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.filters import CommandStart


api = ""
bot = Bot(token=api)
dp = Dispatcher(storage= MemoryStorage())

@dp.message(CommandStart())
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')



@dp.message()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
