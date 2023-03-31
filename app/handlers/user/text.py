from aiogram import Bot, Router
from aiogram.types import Message

from app.db.functions import User

router = Router()


@router.message()
async def text_handler(message: Message, bot: Bot):
    if message.text == 'Статистика':
        pos = await User.get_top_position(message.from_user.id)
        user = await User.get_data(message.from_user.id)
        refer = await User.get_data(user.refer)
        if not refer:
            refer = User(id=0, name="Unknown")
        text = f"🍅 Ваша статистика:\n\n"
        text += f" - Вы заразили: <b>{len(user.referals)}</b>\n"
        text += f" - Вас заразили: <a href='tg://user?id={user.refer}'>{refer.name}</a>\n"
        text += f" - Всего заражено: <b>{await User.get_count()}</b>\n"
        text += f" - Ваша ссылка для приглашения друзей: <code>https://t.me/tomatoclanbot?start={message.from_user.id}</code>.\n"
        text += f" - Ваша позиция в рейтинге: <b>{pos}</b>"
        return await message.answer(text)
    if message.text == 'Топ':
        top = await User.get_top()
        text = "🍅 Топ 10:\n\n"
        for i, user in enumerate(top):
            text += f"{i+1}. <a href='tg://user?id={user.id}'>{user.name}</a> - {len(user.referals)}\n"
        return await message.answer(text)
    if message.text == 'Профиль':
        user = await User.get_data(message.from_user.id)
        text = f"🍅 Ваш профиль:\n\n"
        text += f" - Имя: <b>{user.name}</b>\n"
        text += f" - Статус: <b>{user.status}</b>\n"
        text += f" - ID: <code>{user.id}</code>\n"
        text += f" - Баланс: <b>{user.balance}</b>\n"
        text += f" - Рефералов: <b>{len(user.referals)}</b>\n"
        text += f" - Реферал: <a href='tg://user?id={user.refer}'>{user.refer}</a>\n"
        text += f" - Вы были заражены: <b>{user.register_date}</b>\n"
        return await message.answer(text)

