# Generated by Django 3.2.7 on 2021-10-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20211023_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Card_Image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
