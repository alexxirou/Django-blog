# Generated by Django 3.0.7 on 2020-07-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200705_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]
