# Generated by Django 3.0.8 on 2020-07-20 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slambookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillup',
            name='image',
            field=models.URLField(),
        ),
    ]