# Generated by Django 3.0.7 on 2020-06-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0005_auto_20200621_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='boss',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
