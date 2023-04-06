from tortoise import fields
from tortoise.models import Model


class User(Model):
    """
    DB model for users.

    Fields:
        id: int
        telegram_id: int
        name: str
        refer: int
        referrals: list
        referral_level: int
        balance: int
        awards: list
        register_date: datetime
        confirmed: bool
        status: str (user, admin)
        is_banned: bool
    """
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField()
    name = fields.CharField(max_length=255, default="Unknown")

    refer = fields.BigIntField()
    referrals = fields.JSONField(default=[])
    referral_level = fields.IntField(default=0)

    balance = fields.IntField(default=0)
    awards = fields.JSONField(default=[])

    register_date = fields.DatetimeField(auto_now_add=True)

    confirmed = fields.BooleanField(default=False)

    status = fields.CharField(max_length=255, default="user")
    is_banned = fields.BooleanField(default=False)


class Awards(Model):
    """
    DB model for awards.

    Fields:
        id: int
        name: str
        count: int
        text: str
        badge: str
        award: int
    """
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255)
    count = fields.IntField()
    text = fields.CharField(max_length=255)
    badge = fields.CharField(max_length=255)
    award = fields.BigIntField()
