# Generated by Django 3.2.16 on 2023-01-02 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.TextField(default='', max_length=100),
        ),
    ]
