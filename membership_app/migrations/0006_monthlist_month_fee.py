# Generated by Django 2.2 on 2020-04-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership_app', '0005_auto_20200405_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlist',
            name='month_fee',
            field=models.IntegerField(default=10000),
        ),
    ]