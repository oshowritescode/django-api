# Generated by Django 5.1.7 on 2025-03-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
            ],
        ),
    ]
