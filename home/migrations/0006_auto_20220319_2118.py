# Generated by Django 3.2.9 on 2022-03-19 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220318_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignmentm',
            old_name='subjetname',
            new_name='subjectname',
        ),
        migrations.RenameField(
            model_name='coursecategorym',
            old_name='coursetype',
            new_name='coursecategory',
        ),
        migrations.RenameField(
            model_name='studentassignmentt',
            old_name='submssiondate',
            new_name='submissiondate',
        ),
        migrations.RenameField(
            model_name='studentsmsm',
            old_name='studentid',
            new_name='smsid',
        ),
        migrations.AddField(
            model_name='crmcomponentm',
            name='studentid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.studentm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsmsm',
            name='smsanswer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
