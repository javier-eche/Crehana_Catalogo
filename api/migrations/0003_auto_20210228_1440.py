# Generated by Django 2.2 on 2021-02-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210228_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('LEVEL1', 'Introductorio'), ('LEVEL2', 'Intermedio'), ('LEVEL3', 'Completo'), ('LEVEL4', 'Avanzado')], max_length=50),
        ),
    ]