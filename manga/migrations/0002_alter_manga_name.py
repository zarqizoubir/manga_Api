# Generated by Django 4.0.8 on 2022-12-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]