# Generated by Django 3.0.7 on 2020-07-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='body1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
