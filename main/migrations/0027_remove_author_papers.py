# Generated by Django 3.2.6 on 2021-09-06 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20210906_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='papers',
        ),
    ]