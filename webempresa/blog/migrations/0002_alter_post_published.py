# Generated by Django 4.1.1 on 2023-01-17 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 21, 34, 20, 891272, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicación'),
        ),
    ]
