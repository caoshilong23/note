# Generated by Django 3.2 on 2022-11-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否活跃'),
        ),
    ]