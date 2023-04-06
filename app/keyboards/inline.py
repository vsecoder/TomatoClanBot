from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_author_keyboard():
    buttons = [
        [InlineKeyboardButton(text="@vsecoder", url="https://t.me/vsecoder")],
        [InlineKeyboardButton(text="@sleroq", url="https://t.me/sleroq")],
    ]
    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()


def get_start_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Подробнее, если непонятно", url="https://telegra.ph/Klan-tomatov-03-30")],
        [InlineKeyboardButton(text="Проверить описание", callback_data="check")],
    ]
    keyboard = InlineKeyboardBuilder(markup=buttons)
    return keyboard.as_markup()
