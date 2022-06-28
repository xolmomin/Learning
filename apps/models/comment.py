from django.contrib.auth import get_user_model
from django.db.models import Model, TextField, ForeignKey, CASCADE

user = get_user_model()

class Comment(Model):
    text = TextField()
    author = ForeignKey(user, on_delete=CASCADE, )