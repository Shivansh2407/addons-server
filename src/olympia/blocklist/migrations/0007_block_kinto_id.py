# Generated by Django 2.2.6 on 2019-12-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocklist', '0006_multiblocksubmit_version_max_length_increase'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='kinto_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]
