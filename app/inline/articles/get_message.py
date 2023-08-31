from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, User


def get_message_article(user: User):
    return InlineQueryResultArticle(
        id="message",
        title="🍅 Сообщение об инфицировании",
        description="💫 Отправит шаблонное сообщение с вашей ссылкой на бота",
        input_message_content=InputTextMessageContent(
            message_text=f"<b>🍅 Вас инфицировали!</b>\n"
            "ℹ️ Теперь вам необходимо запустить бота и следовать инструкциям.\n"
            f"<b>🔗 Ссылка на бота:</b> <a href='https://t.me/tomatoclanbot?start={user.id}'>https://t.me/tomatoclanbot</a>.",
            disable_web_page_preview=True,
        ),
    )
