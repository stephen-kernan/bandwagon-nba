# Generated by Django 2.2.2 on 2019-06-23 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandwagon', '0003_auto_20190622_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='./post_pics'),
        ),
    ]