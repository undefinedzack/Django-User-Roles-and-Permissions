# Generated by Django 3.1.7 on 2021-03-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=300)),
                ('mobile_no', models.IntegerField()),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=200)),
                ('department_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('add_user', models.BooleanField(default=False)),
                ('delete_user', models.BooleanField(default=False)),
                ('view_all_user', models.BooleanField(default=False)),
                ('edit_user', models.BooleanField(default=False)),
                ('view_statistics', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=True)),
            ],
        ),
    ]
