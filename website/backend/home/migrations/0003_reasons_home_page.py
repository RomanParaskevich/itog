# Generated by Django 3.2.16 on 2022-11-04 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_reasons_recommendations'),
    ]

    operations = [
        migrations.AddField(
            model_name='reasons',
            name='home_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homepage', verbose_name='Страница (привязка)'),
        ),
    ]
