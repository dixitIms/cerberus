# Generated by Django 4.1.1 on 2022-09-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_name_users_username_users_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='users',
            name='contact',
            field=models.CharField(default='', max_length=12),
        ),
    ]
