# Generated by Django 2.1.3 on 2018-12-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feemanager',
            name='money',
            field=models.IntegerField(default=10000),
        ),
    ]
