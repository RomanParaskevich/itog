# Generated by Django 3.2.16 on 2022-11-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_reasons_recommendations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reasons',
            name='recommendations',
            field=models.JSONField(default=''),
        ),
    ]
