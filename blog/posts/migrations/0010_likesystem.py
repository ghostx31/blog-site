# Generated by Django 3.1.5 on 2021-02-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_userprofile_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
            ],
        ),
    ]
