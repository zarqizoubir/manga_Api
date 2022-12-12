from rest_framework import serializers

from manga import models


class ChapterPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ChapterPart
        exclude = [
            "chapter",
            "id"
        ]


class ChapterSerialzer(serializers.ModelSerializer):
    chapter_parts = ChapterPartSerializer(
        allow_null=True, many=True, required=False)

    class Meta:
        model = models.Chapter
        read_only_fields = ["chapter_parts"]
        exclude = [
            "name",
            "id",
            "manga",
            "created_at"
        ]
