# Generated by Django 3.0.5 on 2020-04-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0003_auto_20200402_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='prof',
            field=models.CharField(max_length=31),
        ),
    ]
