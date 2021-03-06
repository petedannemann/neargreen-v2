# Generated by Django 2.1.4 on 2018-12-27 19:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('address', models.TextField(blank=True, max_length=120, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
