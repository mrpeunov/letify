# Generated by Django 3.2.5 on 2021-07-02 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20210701_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='creator',
        ),
    ]