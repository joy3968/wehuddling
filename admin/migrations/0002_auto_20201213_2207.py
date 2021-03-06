# Generated by Django 3.1.4 on 2020-12-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_tbl',
            old_name='c_address',
            new_name='c_address_detail',
        ),
        migrations.RenameField(
            model_name='customer_tbl',
            old_name='c_birth',
            new_name='c_zip_code',
        ),
        migrations.AddField(
            model_name='customer_tbl',
            name='c_new_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer_tbl',
            name='c_old_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
