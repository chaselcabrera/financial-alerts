# Generated by Django 5.0.4 on 2024-04-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiontype',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
