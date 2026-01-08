import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = 8581470622:AAE8imYsT8uqyRxAu6zBoG0zTPaHKp3z2lc

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("Бот работает!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
