# Generated by Django 4.1.3 on 2024-05-03 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_blaster_notsent_bulkdata_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bulkdata',
            old_name='mobile_number',
            new_name='Mobile',
        ),
    ]
