from aiogram import Bot, Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import CallbackQuery
from app.keyboards.reply import main_menu
from app.db.functions import User, _, Awards
import requests

router = Router()


async def check_awards(user_id: int, bot: Bot):
    awards = await Awards.check_award(user_id)
    for award in awards:
        await bot.send_message(
            user_id,
            f"🎁<b> Вы получили награду по достижению кол-ва заражённых в {award.count}!</b>\n"
            f"Сообщение от создателя: <i>{award.text}</i>\n\n"
            f" Значок: {award.badge}\n"
            f" Награда: {award.award}",
        )
        await User.add_balance(user_id, award.award)


@router.callback_query()
async def check_profile(c: CallbackQuery, bot: Bot):
    html = requests.get(f"https://t.me/{c.from_user.username}").text
    user = await User.get_data(c.from_user.id)

    if "томат" in html.lower():
        await User.confirm(c.from_user.id)
        await c.message.delete()
        kb = await main_menu()

        try:
            await check_awards(user.refer, bot)
            await bot.send_message(
                user.refer,
                f"🍅 <a href='tg://user?id={c.from_user.id}'>{_(c.from_user.full_name)}</a> заражён(-а) вами!",
                parse_mode="HTML"
            )
        except TelegramAPIError:
            pass

        return await bot.send_message(
            c.from_user.id,
            "🍅 Ваш аккаунт подтверждён!",
            reply_markup=kb
        )

    await c.answer("❗️ Слова \"томат\" нет в вашем описании, или у вас нет username!")
