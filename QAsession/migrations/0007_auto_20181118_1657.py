# Generated by Django 2.0 on 2018-11-18 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QAsession', '0006_auto_20181118_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='qa',
            new_name='ans',
        ),
        migrations.AlterField(
            model_name='question',
            name='qa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QAsession.qasession'),
        ),
    ]
