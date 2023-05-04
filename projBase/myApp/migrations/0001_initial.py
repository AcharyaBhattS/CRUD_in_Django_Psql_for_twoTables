# Generated by Django 4.2 on 2023-05-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('room_no', models.IntegerField()),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bill_date', models.DateField()),
                ('amount_paid', models.FloatField()),
            ],
            options={
                'db_table': 'invoice',
                'managed': False,
            },
        ),
    ]
