# Generated by Django 3.1.4 on 2020-12-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0005_auto_20201215_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='shipper_tbl',
            fields=[
                ('sp_no', models.AutoField(primary_key=True, serialize=False)),
                ('sp_name', models.CharField(blank=True, max_length=100, null=True)),
                ('sp_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('sp_city', models.CharField(blank=True, max_length=100, null=True)),
                ('sp_borough', models.CharField(blank=True, max_length=100, null=True)),
                ('sp_join', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
