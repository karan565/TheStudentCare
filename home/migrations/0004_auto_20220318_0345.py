# Generated by Django 3.2.9 on 2022-03-17 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220318_0343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='auserid',
            new_name='userid',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='altemailid',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='caddressline1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='caddressline2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='ccityid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ccityid', to='home.citym'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='clandmark',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='paddressline1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='paddressline2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pcityid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pcityid', to='home.citym'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='plandmark',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='usertype',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Faculty'), ('3', 'Student')], default=1, max_length=50),
        ),
    ]
