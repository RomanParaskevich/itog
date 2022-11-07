# Generated by Django 3.2.16 on 2022-11-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_reasons_recommendations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reasons',
            name='recommendations',
        ),
        migrations.AddField(
            model_name='reasons',
            name='recommendation_description_1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='reasons',
            name='recommendation_description_2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='reasons',
            name='recommendation_description_3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='reasons',
            name='recommendation_title_1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reasons',
            name='recommendation_title_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reasons',
            name='recommendation_title_3',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
