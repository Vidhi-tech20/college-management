# Generated by Django 4.1.2 on 2022-11-10 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_otp_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 11, 10, 43, 4139, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterUniqueTogether(
            name='classattendance',
            unique_together={('assign', 'date')},
        ),
    ]