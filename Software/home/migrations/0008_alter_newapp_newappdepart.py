# Generated by Django 4.0.5 on 2022-07-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_newapp_newappdepart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newapp',
            name='newappdepart',
            field=models.CharField(max_length=255),
        ),
    ]
