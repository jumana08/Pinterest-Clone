# Generated by Django 3.2.6 on 2021-11-10 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterest_clone', '0009_alter_user1_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
