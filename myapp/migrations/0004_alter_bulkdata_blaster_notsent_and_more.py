# Generated by Django 4.1.3 on 2024-05-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_bulkdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkdata',
            name='blaster_notsent',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='blaster_sent',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='rank',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='whatsapp_active',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bulkdata',
            name='whatsapp_inactive',
            field=models.CharField(max_length=20),
        ),
    ]