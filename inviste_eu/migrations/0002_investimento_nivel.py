# Generated by Django 4.1.3 on 2022-11-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inviste_eu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
    ]
