# Generated by Django 3.2.16 on 2022-11-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_bron_date_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bron',
            name='date_out',
            field=models.DateField(blank=True, verbose_name='Дата выезда'),
        ),
    ]
