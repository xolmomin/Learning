from django.db.models import Model, CharField


class Course(Model):
    title = CharField(max_length=128)
