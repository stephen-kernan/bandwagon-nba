# Generated by Django 2.2.2 on 2019-06-23 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandwagon', '0004_auto_20190622_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='./media/post_pics'),
        ),
    ]
