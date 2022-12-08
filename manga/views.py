from rest_framework import generics
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from .models import Manga
from . import serializers


class MangaListCreateApiView(generics.ListCreateAPIView):
    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        route = serializer.validated_data.get("route")
        title = serializer.validated_data.get("title")
        if serializer.validated_data.get("poster"):
            def renamePoster(title: str):
                return title.lower().replace(" ", "_")+".png"
            serializer.validated_data.get("poster").name = renamePoster(title)
        route = title.lower().replace(" ", "_")
        serializer.save(route=route)


class MangaUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = serializers.MangaSerializer
    lookup_field = "route"

    def perform_update(self, serializer):
        route = serializer.validated_data.get("route")
        title = serializer.validated_data.get("title")

        if serializer.validated_data.get("poster"):
            def renamePoster(title: str):
                return title.lower().replace(" ", "_")+".png"
            serializer.validated_data.get("poster").name = renamePoster(title)
        route = title.lower().replace(" ", "_")
        serializer.save(route=route)


class ChapterListCreate(generics.ListCreateAPIView):
    queryset = Manga.objects
    serializer_class = serializers.ChapterSerialzer
    lookup_field = "route"

    def list(self, request: HttpRequest, *args, **kwargs):
        lookup_key = kwargs[self.lookup_field]
        chapters = self.queryset.filter(
            route=lookup_key).first().chapters.all()
        serializer = serializers.ChapterSerialzer(instance=chapters, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer: serializers.ChapterSerialzer):
        lookup_key = self.kwargs[self.lookup_field]
        manga = self.queryset.filter(route=lookup_key).first()
        serializer.save(manga=manga)
