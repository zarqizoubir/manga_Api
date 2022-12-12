from rest_framework import serializers

from . import models
from chapters.serializers import ChapterSerialzer


class MangaSerializer(serializers.ModelSerializer):
    chapters = ChapterSerialzer(allow_null=True, many=True, required=False)

    class Meta:
        model = models.Manga
        read_only_fields = ["chapters", "id_name"]
        exclude = [
            "endpoint",
            "updated_at",
            "uploaded_at"

        ]


class MangaSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Manga

        exclude = [
            "updated_at",
            "uploaded_at"
        ]
