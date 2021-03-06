# Generated by Django 3.1.1 on 2020-09-27 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='boards.board'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
            preserve_default=False,
        ),
    ]
