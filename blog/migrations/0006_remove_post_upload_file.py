# Generated by Django 3.0.7 on 2020-07-05 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200705_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload_file',
        ),
    ]
