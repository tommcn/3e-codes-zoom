# Generated by Django 3.0.4 on 2020-04-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0007_auto_20200410_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='classe_groupe',
            field=models.CharField(help_text='Classe concerné par le cours', max_length=15),
        ),
    ]
