# Generated by Django 4.0.8 on 2022-12-13 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0002_manga_chapters_endpoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='description',
        ),
    ]
