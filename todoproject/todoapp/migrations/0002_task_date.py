# Generated by Django 3.2.7 on 2021-10-15 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-04-22'),
            preserve_default=False,
        ),
    ]
