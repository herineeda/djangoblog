# Generated by Django 2.2.3 on 2019-07-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lion',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]