# Generated by Django 4.0.5 on 2022-07-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_addexam_examsemtype_alter_addexam_regularback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addexam',
            name='examsemtype',
            field=models.CharField(blank=True, default='', max_length=122),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addexam',
            name='regularback',
            field=models.CharField(blank=True, default='', max_length=122),
            preserve_default=False,
        ),
    ]
