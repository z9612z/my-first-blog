# Generated by Django 2.2.6 on 2019-11-16 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_checkbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='checkbox',
            field=models.BooleanField(),
        ),
    ]