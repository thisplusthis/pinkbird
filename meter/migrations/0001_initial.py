# Generated by Django 3.1.1 on 2020-10-01 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('fan', models.BooleanField(default=False)),
            ],
        ),
    ]
