# Generated by Django 4.0.5 on 2022-07-06 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_members_lesson_slug_alter_course_slug_and_more'),
        ('users', '0002_reward_user_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='members',
            field=models.ManyToManyField(related_name='students', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('instructor', 'instructor'), ('student', 'student')], max_length=18),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
