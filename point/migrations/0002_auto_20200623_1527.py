# Generated by Django 3.0.7 on 2020-06-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='ep',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='gp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='ep',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='score',
            name='gp',
            field=models.FloatField(),
        ),
    ]