# Generated by Django 4.0.6 on 2022-07-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0002_alter_chessmatch_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='chessmatch',
            name='result',
            field=models.IntegerField(choices=[(0, 'Draw'), (1, 'White wins'), (-1, 'Black wins')], default=0),
        ),
    ]