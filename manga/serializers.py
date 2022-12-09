from rest_framework import serializers

from . import models


class ChapterSerialzer(serializers.ModelSerializer):

    class Meta:
        model = models.Chapter
        exclude = [
            "id",
            "manga",
            "created_at"
        ]


class MangaSerializer(serializers.ModelSerializer):
    # chapters = ChapterSerialzer(allow_null=True, many=True, required=False)

    class Meta:
        model = models.Manga
        # read_only_fields = ["chapters"]
        exclude = [
            "id_name",
            "updated_at",
            "uploaded_at"
        ]
