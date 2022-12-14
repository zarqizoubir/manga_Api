# Generated by Django 4.0.8 on 2022-12-11 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, unique=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=200, unique=True)),
                ('poster', models.FileField(max_length=400, null=True, upload_to='posters/%Y/%m/%d')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('endpoint', models.URLField(blank=True, max_length=2000, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('rating', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('painter', models.CharField(blank=True, max_length=200)),
                ('type', models.CharField(blank=True, max_length=200)),
                ('release_year', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChapterPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('image', models.ImageField(max_length=1000, null=True, upload_to='chapters/%Y/%m/%d')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter_parts', to='manga.chapter', to_field='name')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='manga.manga', to_field='id_name'),
        ),
    ]
