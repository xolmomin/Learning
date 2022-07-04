from ckeditor.fields import RichTextField
from django.db.models import Model, DateTimeField, TextField, CharField, ForeignKey, ManyToManyField, IntegerField, \
    DecimalField, CASCADE

from apps.users.models import User


class IntegerRangeField(IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    description = TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    title = CharField(max_length=128)
    rating = IntegerRangeField(min_value=1, max_value=5)
    out = DateTimeField(null=True, help_text="When the cow went OUT TO Pasture.")
    _in = DateTimeField(null=True, help_text="When the cow got back IN FROM Pasture.")
    price = DecimalField(max_digits=12, decimal_places=2)
    author = ForeignKey(User, on_delete=CASCADE, related_name="author")
    members = ManyToManyField(User, related_name="members")
    description = RichTextField()

    def duration(self):
        return self.out - self._in


class Chapter(BaseModel):
    title = CharField(max_length=128)
    ForeignKey(Course, on_delete=CASCADE)


class Lesson(BaseModel):
    title = CharField(max_length=128)
    _in = DateTimeField(null=True)
    out = DateTimeField(null=True)
    price = DecimalField(max_digits=12, decimal_places=2)
    chapter = ForeignKey(Chapter, on_delete=CASCADE)

    def duration(self):
        return self.out - self._in


class Comment(BaseModel):
    course = ForeignKey(Course, on_delete=CASCADE)
