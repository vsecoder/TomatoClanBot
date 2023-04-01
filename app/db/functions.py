from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models


def _(text):
    return text.replace('<', '').replace('>', '')

class User(models.User):
    @classmethod
    async def is_registered(cls, telegram_id: int) -> Union[models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def register(cls, telegram_id, refer: int = 0, status: str = "user", name: str = "Unknown"):
        referal_level = 1

        if refer:
            refer = await cls.is_registered(refer)
            if refer:
                referal_level = refer.referal_level + 1
            refer = refer.telegram_id if refer else 0

        await User(
            telegram_id=telegram_id,
            refer=int(refer),
            referal_level=referal_level,
            status=status,
            name=_(name)
            ).save()

    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()
    
    @classmethod
    async def get_data(cls, telegram_id: int) -> Union[models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False
        
    @classmethod
    async def add_referal(cls, refer: int, telegram_id: int):
        user = await cls.get(telegram_id=telegram_id)
        user.referals.append(refer)
        await user.save()

    @classmethod
    async def get_status(cls, telegram_id: int) -> str:
        user = await cls.get(telegram_id=telegram_id)
        return user.status
    
    @classmethod
    async def confirm(cls, telegram_id: int):
        user = await cls.get(telegram_id=telegram_id)
        user.confirmed = True
        await cls.add_referal(telegram_id, user.refer)
        await user.save()

    @classmethod
    async def is_confirmed(cls, telegram_id: int) -> bool:
        user = await cls.get(telegram_id=telegram_id)
        return user.confirmed
    
    @classmethod
    async def get_top_position(cls, telegram_id: int) -> int:
        users = await cls.all()
        users = sorted(users, key=lambda x: len(x.referals), reverse=True)
        for i, user in enumerate(users):
            if user.telegram_id == telegram_id:
                return i + 1
        return 0
    
    @classmethod
    async def get_top(cls, limit: int = 10) -> list:
        users = await cls.all()
        users = sorted(users, key=lambda x: len(x.referals), reverse=True)
        return users[:limit]

