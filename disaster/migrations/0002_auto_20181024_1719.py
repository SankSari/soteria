# Generated by Django 2.1.2 on 2018-10-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name (Strictly Lowercase)'),
        ),
    ]
