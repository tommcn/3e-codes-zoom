# Generated by Django 3.0.5 on 2020-04-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=127)),
                ('classe_groupe', models.CharField(max_length=2)),
                ('prof', models.CharField(max_length=2)),
                ('commnence', models.DateTimeField()),
                ('fini', models.DateTimeField()),
            ],
        ),
    ]
