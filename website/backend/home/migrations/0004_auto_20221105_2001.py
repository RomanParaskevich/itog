# Generated by Django 3.2.16 on 2022-11-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reasons_home_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='reasons',
            name='reasons_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reasons',
            name='recommendations',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Recommendations',
        ),
    ]
