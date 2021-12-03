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

ikkinchi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Andijon-Toshkent-Andijon"), KeyboardButton(text="Farg'ona-Toshkent-Farg'ona")],
        [KeyboardButton(text="Buxoro-Toshkent-Buxoro"), KeyboardButton(text="Jizzax-Toshkent-Jizzax")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)