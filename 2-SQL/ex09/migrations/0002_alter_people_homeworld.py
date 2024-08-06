# Generated by Django 3.2.3 on 2024-08-06 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='ex09.planets', to_field='name'),
        ),
    ]
