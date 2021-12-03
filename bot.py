from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from buttum import menu, birinchi, ikkinchi

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Salom {user}", reply_markup=menu)

@dp.message_handler(Text(equals=["Haydovchi kerak"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=men_haydovchiman)

@dp.message_handler(Text(equals=["Men haydovchiman"]))
async def contacts(message: types.Message):
    await message.answer(f"Qaysi yo'nalishda qatnaysiz?", reply_markup=men_haydovchiman)


@dp.message_handler(Text(equals=["Obuna bo'lish"]))
async def send_contact(message: types.Message):
    msg = "<b>Hamkorlarimizga obuna bo'ling</b>\n@Motivatsiya_Official_TG\n<a href='https://t.me/BekoDev'><u>Python</u></a>"
    await message.answer(msg, parse_mode='html')

@dp.message_handler(Text(equals=["Qo'shimcha fikrlar"]))
async def comments(message: types.Message):
    msg = "Fikrlaringizni <a href='https://t.me/Bekzod_Rakhimov'>admin</a>ga jo'nating"
    await message.answer(msg, parse_mode="html")


@dp.message_handler(Text(equals=["Rasmlar"]))
async def images(message: types.Message):
    await message.answer_photo("https://api.modme.uz/uploads/RYXg4SOLokaorH91.jpg", caption="Data o'quv markazi ikonkasi")
    await message.answer_photo(photo=open('/media/bekzod/Hard Disk6/Python Code/python_darslar/Python/bot/translatebot/tgbot.jpg', 'rb'), caption="Telegram BOT")



@dp.message_handler(Text(equals=["🔙 Orqaga"]))
async def back(message: types.Message):
    await message.answer("Bosh menyu", reply_markup=menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)