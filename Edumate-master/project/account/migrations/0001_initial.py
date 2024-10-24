# Generated by Django 4.1.2 on 2022-11-07 12:19

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('userID', models.IntegerField(unique=True, verbose_name='User ID')),
                ('name', models.CharField(max_length=200)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_stu', models.BooleanField(default=False)),
                ('is_tea', models.BooleanField(default=False)),
                ('otp', models.CharField(blank=True, max_length=4, null=True)),
                ('otp_created_at', models.DateTimeField(default=datetime.datetime(2022, 11, 7, 12, 18, 23, 67293, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssignClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Assign Classes',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('section', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('lastedit', models.DateTimeField(auto_now=True)),
                ('showto', models.IntegerField(default=3)),
            ],
            options={
                'ordering': ['-lastedit'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='teachers/')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.department')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('code', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('department', models.ManyToManyField(to='account.department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, default='', null=True, upload_to='students/')),
                ('blood_group', models.CharField(blank=True, max_length=20, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('student_phone', models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('father_name', models.CharField(blank=True, max_length=200, null=True)),
                ('father_phone', models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('mother_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_phone', models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.class')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.department'),
        ),
        migrations.CreateModel(
            name='AssignTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('7:30 - 8:30', '7:30 - 8:30'), ('8:30 - 9:30', '8:30 - 9:30'), ('9:30 - 10:30', '9:30 - 10:30'), ('11:00 - 11:50', '11:00 - 11:50'), ('11:50 - 12:40', '11:50 - 12:40'), ('12:40 - 1:30', '12:40 - 1:30'), ('2:30 - 3:30', '2:30 - 3:30'), ('3:30 - 4:30', '3:30 - 4:30'), ('4:30 - 5:30', '4:30 - 5:30')], default='11:00 - 11:50', max_length=50)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=15)),
                ('assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.assignclass')),
            ],
        ),
        migrations.AddField(
            model_name='assignclass',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.class'),
        ),
        migrations.AddField(
            model_name='assignclass',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.subject'),
        ),
        migrations.AddField(
            model_name='assignclass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignclass_teacher', to='account.teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='assignclass',
            unique_together={('subject', 'class_id', 'teacher')},
        ),
    ]
