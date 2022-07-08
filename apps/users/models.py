from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, ImageField, ManyToManyField, ForeignKey, CASCADE

from shared.models import BaseModel


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a email!')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    INSTRUCTOR = 'instructor'
    STUDENT = 'student'
    ROLES = (
        (INSTRUCTOR, 'instructor'),
        (STUDENT, 'student')
    )
    username = CharField(max_length=255)
    email = EmailField(unique=True)
    role = CharField(max_length=18, choices=ROLES)

    reward = ManyToManyField('Reward', 'users')
    members = ManyToManyField('courses.Course', 'students')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Reward(BaseModel):
    name = CharField(max_length=56)
    logo = ImageField(upload_to='reward-logos/')


class Certificate(BaseModel):
    title = CharField(max_length=128)
    owner = ForeignKey(User, CASCADE)
