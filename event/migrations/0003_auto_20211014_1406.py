# Generated by Django 3.2.8 on 2021-10-14 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_part'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
    ]