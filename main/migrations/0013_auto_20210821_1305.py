# Generated by Django 3.2.6 on 2021-08-21 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_paper_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paper',
            options={'ordering': ['-year']},
        ),
        migrations.RemoveField(
            model_name='author',
            name='papers',
        ),
        migrations.AlterOrderWithRespectTo(
            name='paper',
            order_with_respect_to=None,
        ),
    ]
