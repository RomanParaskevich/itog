# Generated by Django 3.2.16 on 2022-11-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_auto_20221106_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelpage',
            name='stars',
            field=models.CharField(choices=[('<li></li>', '1 звезда'), ('<li></li><li></li>', '2 звезды'), ('<li></li><li></li><li></li>', '3 звезды'), ('<li></li><li></li><li></li><li></li>', '4 звезды'), ('<li></li><li></li><li></li><li></li><li></li>', '5 звезд')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
    ]
