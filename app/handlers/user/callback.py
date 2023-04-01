from aiogram import Bot, Router
from aiogram.types import CallbackQuery
from app.keyboards.reply import main_menu
from app.db.functions import User, _
import requests

router = Router()


@router.callback_query()
async def check_profile(c: CallbackQuery, bot: Bot):
    html = requests.get(f"https://t.me/{c.from_user.username}").text
    user = await User.get_data(c.from_user.id)

    if "томат" in html.lower():
        await User.confirm(c.from_user.id)
        await c.message.delete()
        kb = await main_menu()

        try:
            await bot.send_message(
                user.refer,
                f"🍅 <a href='tg://user?id={c.from_user.id}'>{_(c.from_user.full_name)}</a> заражён(-а) вами!",
                parse_mode="HTML"
            )
        except:
            pass

        return await bot.send_message(
            c.from_user.id,
            "🍅 Ваш аккаунт подтверждён!",
            reply_markup=kb
        )

    await c.answer("❗️ Слова \"томат\" нет в вашем описании.")
