# Generated by Django 2.1.2 on 2018-12-19 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20181219_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=100),
        ),
    ]
