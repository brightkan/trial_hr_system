# Generated by Django 5.1.1 on 2024-10-07 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('other_names', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('id_photo', models.TextField(blank=True, null=True)),
                ('employee_number', models.CharField(max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='StaffCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('is_used', models.BooleanField(default=False)),
                ('staff_member', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staffmember')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
