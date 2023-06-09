# Generated by Django 4.1.7 on 2023-05-26 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0011_alter_sample_table_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='recurring_invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_supply', models.CharField(max_length=255)),
                ('entry_type', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('order_num', models.CharField(max_length=255)),
                ('every', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('terms', models.CharField(max_length=255)),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
            ],
        ),
    ]
