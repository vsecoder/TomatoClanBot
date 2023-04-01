from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Column, Url
from aiogram_dialog.widgets.text import Const, Format

class StartingDialog(StatesGroup):
    greeting = State()


async def checker(c: CallbackQuery, _: Button, manager: DialogManager):
    await c.answer("❗️ Тестовое уведомление", show_alert=True, cache_time=0)
    await c.message.delete()
    await manager.done()


ui = Dialog(
    Window(
        Format("🍅 Приветствую тебя в клан-игре <b>«Клан томатов»</b>!\n\n<b>ℹ️ Для продолжения напиши/добавь в описание</b> \"<code>напиши в лс томат</code>\""),
        Column(
            Url(Const("Обязательно к прочтению"), Const("https://telegra.ph/Klan-tomatov-03-30")),
            Button(Const("Проверить"), id="test_button", on_click=checker),
        ),
        state=StartingDialog.greeting,
    ),
)
