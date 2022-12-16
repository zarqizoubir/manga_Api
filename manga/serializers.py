from rest_framework import serializers

from . import models
from chapters.serializers import ChapterSerialzer


class MangaSerializer(serializers.ModelSerializer):
    chapters = ChapterSerialzer(allow_null=True, many=True, required=False)

    class Meta:
        model = models.Manga
        read_only_fields = ["chapters", "id_name", "chapters_endpoint", ]
        exclude = [
            "endpoint",
            "updated_at",
            "uploaded_at"

        ]

    def update(self, instance, validated_data):

        if validated_data["poster"] == None:
            validated_data["poster"] = instance.poster
            print(validated_data)

        return super().update(instance, validated_data)


class MangaSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Manga
        read_only_fields = ["id_name"]
        exclude = [
            "updated_at",
            "uploaded_at"
        ]
