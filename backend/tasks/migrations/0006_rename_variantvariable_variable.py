# Generated by Django 3.2.5 on 2021-07-02 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_option_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VariantVariable',
            new_name='Variable',
        ),
    ]