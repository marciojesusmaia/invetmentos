# Generated by Django 4.1.3 on 2022-11-17 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inviste_eu', '0002_investimento_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='nivel',
        ),
    ]
