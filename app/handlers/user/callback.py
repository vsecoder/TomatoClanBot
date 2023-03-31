from aiogram import Bot, Router
from aiogram.types import CallbackQuery
from app.keyboards.reply import main_menu
from app.db.functions import User
import requests

router = Router()


# callback
@router.callback_query()
async def check_profile(c: CallbackQuery, bot: Bot):
    html = requests.get(f"https://t.me/{c.from_user.username}").text
    
    if "томат" in html.lower():
        await User.confirm(c.from_user.id)
        await c.message.delete()
        kb = await main_menu()
        return await bot.send_message(
            c.from_user.id,
            "🍅 Ваш аккаунт подтверждён!",
            reply_markup=kb
        )

    await c.answer("❗️ Слова \"томат\" нет в вашем описании.")