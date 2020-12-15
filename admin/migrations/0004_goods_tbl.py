# Generated by Django 3.1.4 on 2020-12-13 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_company_tbl_cp_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods_tbl',
            fields=[
                ('gd_no', models.AutoField(primary_key=True, serialize=False)),
                ('gd_category', models.CharField(blank=True, max_length=100, null=True)),
                ('gd_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gd_price', models.IntegerField(blank=True, null=True)),
                ('gd_stock', models.IntegerField(blank=True, null=True)),
                ('gd_img', models.ImageField(blank=True, null=True, upload_to='goods/')),
                ('gd_desc', models.TextField(blank=True, max_length=500, null=True)),
                ('gd_join', models.DateField(auto_now_add=True)),
                ('cp_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.company_tbl')),
            ],
        ),
    ]