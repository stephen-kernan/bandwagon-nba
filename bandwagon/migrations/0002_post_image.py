# Generated by Django 2.2.2 on 2019-06-23 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandwagon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]
