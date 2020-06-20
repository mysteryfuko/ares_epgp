# Generated by Django 3.0.7 on 2020-06-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('boss', models.CharField(max_length=40)),
                ('party', models.TextField()),
                ('dkp', models.IntegerField()),
                ('ep', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='loot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
                ('item', models.IntegerField()),
                ('dkp', models.IntegerField()),
                ('gp', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('kill', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='point',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('job', models.CharField(max_length=10)),
                ('dkp', models.IntegerField()),
                ('ep', models.IntegerField()),
                ('gp', models.IntegerField()),
            ],
        ),
    ]