# Generated by Django 2.0.2 on 2020-04-06 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='create',
            name='no',
            field=models.IntegerField(default=1),
        ),
    ]
