# Generated by Django 3.2.9 on 2021-11-16 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group_details', '0003_alter_delivaries_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivaries',
            old_name='status',
            new_name='payment_status',
        ),
    ]
