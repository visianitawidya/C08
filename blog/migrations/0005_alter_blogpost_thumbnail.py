# Generated by Django 3.2.8 on 2021-11-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211029_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/blog'),
        ),
    ]
