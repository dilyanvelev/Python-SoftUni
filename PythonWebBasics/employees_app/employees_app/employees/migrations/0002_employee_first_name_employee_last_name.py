# Generated by Django 4.2.6 on 2023-10-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
