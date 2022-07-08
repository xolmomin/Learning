from ckeditor.fields import RichTextField
from django.db.models import Model, DateTimeField, CharField, ForeignKey, ManyToManyField, IntegerField, \
    DecimalField, CASCADE, ImageField, BooleanField, SlugField
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# from apps.users.models import User
from shared.models import BaseModel, DescriptionBaseModel


class IntegerRangeField(IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class CourseCategory(BaseModel):
    title = CharField(max_length=128)
    slug = SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title


class Tag(BaseModel):
    name = CharField(max_length=28)
    slug = SlugField(unique=True)

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #         while Tag.objects.filter(slug=self.slug).exists():
    #             self.slug = f'{self.slug}-1'
    #
    #     super().save(force_insert, force_update, using, update_fields)

class Course(BaseModel):
    title = CharField(max_length=128)
    rating = IntegerRangeField(min_value=1, max_value=5)
    price = DecimalField(max_digits=12, decimal_places=2)
    _in = DateTimeField(null=True)
    out = DateTimeField(null=True)
    author = ForeignKey('users.User', CASCADE, "author")
    description = RichTextField()
    logo = ImageField(upload_to='course-logos/', default='path/to/my/default/image.jpg')
    picture = ImageField(upload_to='course-picures/', default='path/to/my/default/image.jpg')
    tags = ManyToManyField("Tag", 'courses')
    slug = SlugField(unique=True, default='')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
            while Course.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)

    def duration(self):
        return self.out - self._in


class FeedBack(DescriptionBaseModel):
    title = CharField(max_length=56)


class Chapter(DescriptionBaseModel):
    title = CharField(max_length=128)
    ForeignKey(Course, CASCADE, "chapters")


class Lesson(DescriptionBaseModel):
    title = CharField(max_length=128)
    price = DecimalField(max_digits=12, decimal_places=2)
    chapter = ForeignKey(Chapter, CASCADE, "lessons")
    duration = IntegerField()
    slug = SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)

        super().save(force_insert, force_update, using, update_fields)


class Comment(DescriptionBaseModel):
    course = ForeignKey(Course, CASCADE)


class Question(BaseModel):
    question = CharField(max_length=256)
    body = RichTextField()
    course = ForeignKey(Course, CASCADE)
    score = CharField(max_length=12)

    # class Meta:
    #     index_together = ('question', 'score')


class Answer(DescriptionBaseModel):
    question = ForeignKey(Question, CASCADE)
    is_true = BooleanField(default=False)


class ForumCategory(DescriptionBaseModel):  # Form
    title = CharField(max_length=128)
    course = ForeignKey(Course, CASCADE)


class Forum(MPTTModel):
    category = ForeignKey(ForumCategory, CASCADE)
    parent = TreeForeignKey('self', CASCADE, 'children')
    user = ForeignKey('users.User', CASCADE)
