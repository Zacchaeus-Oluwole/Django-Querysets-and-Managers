# Generated by Django 4.0 on 2022-07-29 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='identifier',
            field=models.SlugField(blank=True, max_length=20, unique=True),
        ),
    ]
