from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.filters import CommandStart


api = "7867274709:AAHYgWkZ4GZaYmksMvwwCv4U0iCSoiPnWmw"
bot = Bot(token=api)
dp = Dispatcher(storage= MemoryStorage())

@dp.message(CommandStart())
async def start(message):
   print('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())