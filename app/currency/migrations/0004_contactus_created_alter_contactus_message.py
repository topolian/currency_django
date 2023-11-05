# Generated by Django 4.2.5 on 2023-10-17 13:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=2056),
        ),
    ]
