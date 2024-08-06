# Generated by Django 3.2.3 on 2024-08-06 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0003_alter_people_homeworld'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.PROTECT, to='ex09.planets'),
        ),
    ]
