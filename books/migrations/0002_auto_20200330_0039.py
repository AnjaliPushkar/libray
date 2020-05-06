# Generated by Django 2.0.2 on 2020-03-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.TextField(max_length=255)),
                ('bookname', models.CharField(max_length=255)),
                ('bookid', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='password',
            field=models.TextField(max_length=255),
        ),
    ]
