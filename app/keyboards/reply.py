from aiogram import types

async def main_menu():
    buttons = [
        [
            types.KeyboardButton(text="Статистика"),
            types.KeyboardButton(text="Профиль"),
            types.KeyboardButton(text="Топ")
        ],
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard
