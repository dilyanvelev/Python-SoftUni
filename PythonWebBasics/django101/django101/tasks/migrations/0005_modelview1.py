# Generated by Django 4.2.6 on 2023-10-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_text_model_last_name_rename_title_model_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelView1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=78)),
            ],
        ),
    ]