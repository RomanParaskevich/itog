# Generated by Django 3.2.16 on 2022-11-07 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_bron'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bron',
            old_name='parents',
            new_name='adults',
        ),
        migrations.RenameField(
            model_name='bron',
            old_name='input_date',
            new_name='date_in',
        ),
        migrations.RenameField(
            model_name='bron',
            old_name='output_date',
            new_name='date_out',
        ),
        migrations.RenameField(
            model_name='bron',
            old_name='childrens',
            new_name='kids',
        ),
    ]