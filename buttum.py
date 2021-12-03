from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Haydovchi kerak"), KeyboardButton(text="Pochta yuborish")],
        [KeyboardButton(text="Men haydovchiman"), KeyboardButton(text="Ma'lumotlar")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

birinchi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Toshkent"), KeyboardButton(text="Surxondaryo")],
        [KeyboardButton(text="Xorazm"), KeyboardButton(text="Buxoro")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

men_haydovchiman = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Andijon-Toshkent-Andijon"), KeyboardButton(text="Farg'ona-Toshkent-Farg'ona")],
        [KeyboardButton(text="Buxoro-Toshkent-Buxoro"), KeyboardButton(text="Jizzax-Toshkent-Jizzax")],
        [KeyboardButton(text="Namangan-Toshkent-Namangan"), KeyboardButton(text="Navoi-Toshkent-Navoi")],
        [KeyboardButton(text="Qashqidaryo-Toshkent-Qashqidaryo"), KeyboardButton(text="Qoraqalpoqiston-Toshkent-Qoraqalpaqiston")],
        [KeyboardButton(text="Samarqand-Toshkent-Samarqand"), KeyboardButton(text="Sirdayo-Toshkent-Sirdaryo")],
        [KeyboardButton(text="Surxondaryo-Toshkent-Surxondaryo"), KeyboardButton(text="Xorazm-Toshkent-Xorazm")],
    
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)