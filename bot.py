import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# Вставь сюда свой API-токен
TOKEN = "7832067581:AAGQRlXmVgQRNyw2kxrTQHBTSMn7Ko1v6rs"

# Создаём объект бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список шуток
jokes = [
    "Программисты не спят. Они ждут, пока компилятор закончится.",
    "Почему программисты путают Хэллоуин и Рождество? Потому что 31 октября — это 25 декабря в шестнадцатеричной системе.",
    "Знаешь, какой у меня пароль? **********. Ну ты же не думал, что я тебе скажу его?",
    "Программист заходит в бар, заказывает 1 пиво. Потом 10. Потом 256. Потом 65536...",
    "Как программист заказывает пиццу? - Алло, доставьте мне пиццу. - Какую? - Нормальную.",
]

# Команда /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я Бот-шутник 🤖\nНапиши /joke, и я расскажу тебе айтишную шутку!")

# Команда /joke
@dp.message(Command("joke"))
async def joke_command(message: Message):
    await message.answer(random.choice(jokes))

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
