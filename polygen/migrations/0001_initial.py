# Generated by Django 2.2.1 on 2019-09-01 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PolyPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_lat', models.DecimalField(blank=True, decimal_places=9, max_digits=19, null=True)),
                ('_long', models.DecimalField(blank=True, decimal_places=9, max_digits=19, null=True)),
            ],
        ),
    ]