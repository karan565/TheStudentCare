# Generated by Django 3.2.9 on 2022-03-19 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220319_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentm',
            name='courseid',
        ),
    ]