from django.db import models

# Create your models here.


class Manga(models.Model):
    id_name = models.CharField(unique=True, max_length=200)
    poster = models.FileField(
        upload_to="posters/%Y/%m/%d", max_length=400, null=True)
    name = models.CharField(max_length=300, unique=True)
    endpoint = models.URLField(unique=True, blank=True, max_length=2000)
    chapters_endpoint = models.URLField(
        unique=True, blank=True, max_length=2000)
    description = models.TextField(blank=True, default="")
    rating = models.DecimalField(default=0,
                                 blank=True, decimal_places=2, max_digits=10)
    author = models.CharField(max_length=200, blank=True)

    painter = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    release_year = models.CharField(blank=True, max_length=100)
    status = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Chapter(models.Model):
    name = models.CharField(blank=True, unique=True, max_length=2000)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True)
    manga = models.ForeignKey(Manga, to_field="id_name", related_name="chapters",
                              null=True, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now=True,)

    def __str__(self) -> str:
        return self.title


class ChapterPart(models.Model):
    title = models.CharField(max_length=300, blank=True)
    image = models.ImageField(
        upload_to="chapters/%Y/%m/%d", max_length=1000, null=True)
    chapter = models.ForeignKey(Chapter, to_field="name", related_name="chapter_parts",
                                null=True, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return self.filename
