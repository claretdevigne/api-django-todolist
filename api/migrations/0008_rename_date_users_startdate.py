# Generated by Django 4.1.3 on 2022-12-08 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_users_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='date',
            new_name='startdate',
        ),
    ]
