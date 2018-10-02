# Generated by Django 2.1b1 on 2018-09-28 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='HotJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='TopJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=75)),
            ],
        ),
    ]