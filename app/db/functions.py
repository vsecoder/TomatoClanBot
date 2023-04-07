from typing import Union

from tortoise.exceptions import DoesNotExist

from app.db import models


def _(text):
    return text.replace('<', '').replace('>', '')


class User(models.User):
    """
    User model, contains all methods for working with users.
    """
    @classmethod
    async def is_registered(cls, telegram_id: int) -> Union[models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def register(
        cls,
        telegram_id,
        refer: int = 0,
        status: str = "user",
        name: str = "Unknown"
    ):
        referral_level = 1

        if refer:
            refer = await cls.is_registered(refer)
            if refer:
                referral_level = refer.referral_level + 1
            refer = refer.telegram_id if refer else 0

        await User(
            telegram_id=telegram_id,
            refer=int(refer),
            referal_level=referral_level,
            status=status,
            name=_(name)
            ).save()

    @classmethod
    async def get_count(cls) -> int:
        return await cls.all().count()

    @classmethod
    async def get_all(cls) -> list:
        return await cls.all()

    @classmethod
    async def get_data(cls, telegram_id: int) -> Union[models.User, bool]:
        try:
            return await cls.get(telegram_id=telegram_id)
        except DoesNotExist:
            return False

    @classmethod
    async def add_referral(cls, refer: int, telegram_id: int):
        try:
            user = await cls.get(telegram_id=telegram_id)
            user.referrals.append(refer)
            await user.save()
        except DoesNotExist:
            pass

    @classmethod
    async def get_status(cls, telegram_id: int) -> Union[str, bool]:
        try:
            user = await cls.get(telegram_id=telegram_id)
            return user.status if user else False
        except DoesNotExist:
            return False

    @classmethod
    async def confirm(cls, telegram_id: int):
        user = await cls.get(telegram_id=telegram_id)
        user.confirmed = True
        await cls.add_referral(telegram_id, user.refer)
        await user.save()

    @classmethod
    async def is_confirmed(cls, telegram_id: int) -> bool:
        user = await cls.get(telegram_id=telegram_id)
        return user.confirmed

    @classmethod
    async def get_top_position(cls, telegram_id: int) -> int:
        users = await cls.all()
        users = sorted(users, key=lambda x: len(x.referrals), reverse=True)
        for i, user in enumerate(users):
            if user.telegram_id == telegram_id:
                return i + 1
        return 0

    @classmethod
    async def get_top(cls, limit: int = 10) -> list:
        users = await cls.all()
        users = sorted(users, key=lambda x: len(x.referrals), reverse=True)
        return users[:limit]

    @classmethod
    async def get_awards(cls, telegram_id: int) -> list:
        try:
            user = await cls.get(telegram_id=telegram_id)
            return user.awards
        except DoesNotExist:
            return []

    @classmethod
    async def add_balance(cls, telegram_id: int, amount: int):
        user = await cls.get(telegram_id=telegram_id)
        user.balance += amount
        await user.save()


class Awards(models.Awards):
    """
    Awards is a class for working with awards,
    which are given to users for referrals.
    """
    @classmethod
    async def get_award_by_count(cls, count: int) -> Union[models.Awards, bool]:
        try:
            return await cls.get(count=count)
        except DoesNotExist:
            return False

    @classmethod
    async def get_award_by_name(cls, name: str) -> Union[models.Awards, bool]:
        try:
            return await cls.get(name=name)
        except DoesNotExist:
            return False

    @classmethod
    async def add_award(cls, name: str, count: int, text: str, badge: str, award: int):
        await cls(
            name=name,
            count=count,
            text=text,
            badge=badge,
            award=award
        ).save()

    @classmethod
    async def check_award(cls, telegram_id: int) -> list:
        user = await User.get_data(telegram_id)
        awards = await cls.all()
        awards = sorted(awards, key=lambda x: x.count, reverse=True)

        res = []

        for award in awards:
            if len(user.referrals) >= award.count and award.name not in user.awards:
                user.awards.append(award.name)
                await user.save()
                res.append(award)

        return res

    @classmethod
    async def get_all(cls) -> list:
        return await cls.all()
