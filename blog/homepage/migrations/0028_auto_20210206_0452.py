# Generated by Django 3.1.5 on 2021-02-06 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0027_auto_20210204_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
