# Generated by Django 2.0 on 2018-10-14 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QAsession', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qasession',
            name='close_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='qasession',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='qasession',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]
