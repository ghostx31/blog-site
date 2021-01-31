# Generated by Django 3.1.5 on 2021-01-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20210128_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackclass',
            name='feedback',
            field=models.CharField(choices=[('Comments', 'Comments'), ('Suggestions', 'Suggestions'), ('Questions', 'Questions')], default=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedbackclass',
            name='fname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
