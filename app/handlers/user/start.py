from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.db.functions import User
from app.keyboards.inline import get_start_keyboard
from app.keyboards.reply import main_menu

from app.filters.is_chat import IsChat

router = Router()


async def get_args(message: Message) -> list:
    args = message.text.split(" ")
    if len(args) != 2 or not args[1].isdigit():
        args = [None, 0]
    return args


@router.message(CommandStart(), IsChat(is_chat=False))
async def cmd_start(message: Message, bot: Bot):
    user_id = message.from_user.id
    args = await get_args(message)

    if not await User.is_registered(user_id):
        await User.register(
            user_id,
            status="user",
            refer=args[1] if len(args) > 1 else 0,
            name=message.from_user.full_name,
        )

    if await User.is_confirmed(user_id):
        kb = await main_menu()
        return await message.answer("🍅 Клавиатура активирована!", reply_markup=kb)

    await message.answer_sticker(
        sticker="CAACAgIAAxkBAAEfA1BkJXdai4FJfHezrU8OygyvcA2b2QACawEAAlX9MBHu2ne738b8ry8E"
    )

    await message.answer(
        f"<b>🍅 Вас инфицировали!</b>\n\n"
        f' - Теперь Вы должны написать/добавить в описание: "<code>напиши в лс томат</code>";\n'
        f" - Инфекция должна распространяться тихо;\n"
        f' - Единственное правило - не спойлерить игру другим и не говорить заранее, что будет, если они напишут слово "томат";\n'
        f' - Когда вам напишут в ЛС "томат", вы должны будете повторить действие заразившего Вас(используя inline мод бота);\n'
        f" - Ваша ссылка для приглашения друзей: <code>https://t.me/tomatoclanbot?start={user_id}</code>.\n\n"
        "<b>⚠️ Для ведения статистики необходимо подтвердить описание!\n",
        "ℹ️ Что бы заразить пользователя необходимо просто написать в строку сообщения @tomatoclanbot и нажать на всплывающую кнопку!</b>",
        reply_markup=get_start_keyboard(),
    )
