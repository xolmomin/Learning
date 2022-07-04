from django.db.models import Model, DateTimeField, TextField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    description = TextField(null=True, blank=True)

    class Meta:
        abstract=True


class Course:
    pass


