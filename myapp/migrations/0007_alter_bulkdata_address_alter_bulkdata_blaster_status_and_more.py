# Generated by Django 4.1.3 on 2024-05-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_mobile_number_bulkdata_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkdata',
            name='Address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='Blaster_Status',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='Mobile',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='Name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='Pincode',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='WhatsApp_Status',
            field=models.CharField(max_length=200),
        ),
    ]