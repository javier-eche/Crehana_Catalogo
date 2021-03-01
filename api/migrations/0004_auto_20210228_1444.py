# Generated by Django 2.2 on 2021-02-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210228_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='discount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='real_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
