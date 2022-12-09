from django.contrib import admin

from . import models


admin.site.register(models.Manga)
admin.site.register(models.Chapter)
admin.site.register(models.ChapterPart)
