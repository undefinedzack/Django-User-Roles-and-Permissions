# Generated by Django 3.1.7 on 2021-03-24 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admins',
            new_name='Adminz',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='Userz',
        ),
    ]