# Generated by Django 4.1.3 on 2022-12-06 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_users_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='users',
            name='lastname',
            field=models.CharField(default='lastname', max_length=250),
        ),
    ]
