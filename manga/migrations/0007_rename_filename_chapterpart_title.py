# Generated by Django 4.0.8 on 2022-12-09 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0006_alter_chapter_number_chapterpart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapterpart',
            old_name='filename',
            new_name='title',
        ),
    ]