from aiogram import types
from aiogram.filters import Filter

from app.db.functions import User


class IsOwner(Filter):
    def __init__(self, is_owner: bool) -> None:
        self.is_owner = is_owner

    async def __call__(self, message: types.Message) -> bool:
        status = await User.get_status(message.from_user.id)
        return status == "admin" if self.is_owner else status != "admin"
