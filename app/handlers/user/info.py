from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.config import Config
from app.keyboards.inline import get_author_keyboard

router = Router()


@router.message(Command(commands=["help"]))
async def help_handler(message: Message):
    text = "ℹ️ <b>https://telegra.ph/Klan-tomatov-03-30</b>\n\nЕсли что-то не понятно, пишите @vsecoder"
    await message.answer(text)


@router.message(Command(commands=["about"]))
async def about_handler(message: Message):
    await message.answer(
        "ℹ️ Бот был задуман для развлечения)\nРазработчики и создатели идеи:",
        reply_markup=get_author_keyboard(),
    )
