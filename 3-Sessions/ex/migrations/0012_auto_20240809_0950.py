# Generated by Django 3.2.3 on 2024-08-09 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0011_customuser_is_tip_downvoter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_tip_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_tip_downvoter',
        ),
    ]
