# Generated by Django 2.1.5 on 2019-02-20 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='lsting_id',
            new_name='listing_id',
        ),
    ]
