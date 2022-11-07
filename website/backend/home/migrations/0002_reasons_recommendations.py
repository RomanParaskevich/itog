# Generated by Django 3.2.16 on 2022-11-04 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reasons_title', models.CharField(max_length=100)),
                ('reasons_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation_title', models.CharField(max_length=100)),
                ('recommendation_description', models.TextField()),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.reasons')),
            ],
        ),
    ]
