# Generated by Django 2.1.3 on 2018-12-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership_app', '0002_auto_20181203_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='feemanager',
            name='using',
            field=models.CharField(choices=[('in', '입금'), ('out', '출금')], default='in', max_length=3),
        ),
    ]
