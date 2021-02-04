# Generated by Django 3.1.5 on 2021-02-02 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_auto_20210201_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]