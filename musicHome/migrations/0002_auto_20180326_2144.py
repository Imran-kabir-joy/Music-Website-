# Generated by Django 2.0.3 on 2018-03-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicHome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.DateField(),
        ),
    ]