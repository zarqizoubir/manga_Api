from django.db import models

# Create your models here.


class Manga(models.Model):
    id_name = models.CharField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=300,)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=10)
    author = models.CharField(max_length=200, blank=True)
    painter = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    release_year = models.CharField(blank=True, max_length=100)
    status = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self


class Chapter(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True)
    manga = models.ForeignKey(Manga, to_field="id_name", related_name="chapters",
                              null=True, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now=True,)

    def __str__(self) -> str:
        return self.title
