# Generated by Django 3.2.6 on 2021-08-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_paper_abstract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(max_length=5000),
        ),
    ]
