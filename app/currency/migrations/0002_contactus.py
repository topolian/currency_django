# Generated by Django 4.2.5 on 2023-09-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=70)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=700)),
            ],
        ),
    ]
