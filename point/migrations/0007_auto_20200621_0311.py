# Generated by Django 3.0.7 on 2020-06-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0006_auto_20200621_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='boss',
            field=models.TextField(blank=True, null=True),
        ),
    ]
