# Generated by Django 3.1.7 on 2021-02-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]