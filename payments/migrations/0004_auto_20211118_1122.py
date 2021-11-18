# Generated by Django 3.2.9 on 2021-11-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_payments_add_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='pay_bill',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='phone_number',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
