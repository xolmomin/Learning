from django.db import models
from django.db.models import Model, CharField, ForeignKey, DateTimeField, TextField, CASCADE


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = CharField(max_length=56)
    description = TextField(blank=True, null=True)


class Billing(BaseModel):
    in_name = CharField(max_length=56)
    address = CharField(max_length=128)
    country = ForeignKey(Country, on_delete=CASCADE)