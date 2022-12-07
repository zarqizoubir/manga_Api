# Generated by Django 4.0.8 on 2022-12-07 01:29

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
                ('name', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(blank=True, max_length=500, unique=True)),
                ('poster', models.FileField(max_length=255, upload_to='posters/')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
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
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(max_length=255, upload_to='chapters/screens/')),
                ('chapter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='manga.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='manga.manga'),
        ),
    ]
