# Generated by Django 4.1.5 on 2023-01-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=40, primary_key=True, serialize=False, verbose_name='URL'),
        ),
    ]
