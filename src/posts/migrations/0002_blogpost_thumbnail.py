# Generated by Django 5.1.6 on 2025-03-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
