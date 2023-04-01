from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField()
    name = fields.CharField(max_length=255, default="Unknown")

    # referal system
    refer = fields.BigIntField()
    referals = fields.JSONField(default=[])
    referal_level = fields.IntField(default=0)

    # profile
    balance = fields.IntField(default=0)
    awards = fields.JSONField(default=[])

    register_date = fields.DatetimeField(auto_now_add=True)

    confirmed = fields.BooleanField(default=False)

    status = fields.CharField(max_length=255, default="user")
    is_banned = fields.BooleanField(default=False)

