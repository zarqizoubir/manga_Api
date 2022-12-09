from rest_framework import serializers

from . import models


class ChapterPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterPart
        exclude = [
            "id"
        ]


class ChapterSerialzer(serializers.ModelSerializer):
    chapter_parts = ChapterPartSerializer(
        allow_null=True, many=True, required=False)

    class Meta:
        model = models.Chapter
        read_only_fields = ["chapter_parts"]
        exclude = [
            "id",
            "number",
            "manga",
            "created_at"
        ]


class MangaSerializer(serializers.ModelSerializer):
    chapters = ChapterSerialzer(allow_null=True, many=True, required=False)

    class Meta:
        model = models.Manga
        read_only_fields = ["chapters", "id_name"]
        exclude = [
            "updated_at",
            "uploaded_at"
        ]
