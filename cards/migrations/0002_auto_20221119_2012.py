# Generated by Django 3.2.13 on 2022-11-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupcard',
            name='socks',
        ),
        migrations.AddField(
            model_name='groupcard',
            name='userdeco',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groupcard',
            name='chimneys',
            field=models.IntegerField(blank=True),
        ),
    ]
