# Generated by Django 3.2 on 2022-11-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32, verbose_name='密码'),
        ),
    ]
