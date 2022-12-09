from rest_framework import generics
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from .models import Manga
from . import serializers


# class MangaListCreateApiView(generics.ListCreateAPIView):
#     queryset = Manga.objects.all()
#     serializer_class = serializers.MangaSerializer

#     def perform_create(self, serializer):
#         print(self.request.data)
#         id_manga = serializer.validated_data.get("id_manga")
#         name = serializer.validated_data.get("name")
#         if serializer.validated_data.get("poster"):
#             def renamePoster(title: str):
#                 return title.lower().replace(" ", "_")+".png"
#             serializer.validated_data.get("poster").name = renamePoster(name)
#         id_manga = name.lower().replace(" ", "_")
#         serializer.save(id_manga=id_manga)


# class MangaUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Manga.objects.all()
#     serializer_class = serializers.MangaSerializer
#     lookup_field = "id_manga"

#     def perform_update(self, serializer):
#         id_manga = serializer.validated_data.get("id_manga")
#         name = serializer.validated_data.get("name")

#         if serializer.validated_data.get("poster"):
#             def renamePoster(title: str):
#                 return title.lower().replace(" ", "_")+".png"
#             serializer.validated_data.get("poster").name = renamePoster(name)
#         id_manga = name.lower().replace(" ", "_")
#         serializer.save(id_manga=id_manga)


# class ChapterListCreate(generics.ListCreateAPIView):
#     queryset = Manga.objects
#     serializer_class = serializers.ChapterSerialzer
#     lookup_field = "id_manga"

#     def list(self, request: HttpRequest, *args, **kwargs):
#         lookup_key = kwargs[self.lookup_field]
#         chapters = self.queryset.filter(
#             route=lookup_key).first().chapters.all()
#         serializer = serializers.ChapterSerialzer(instance=chapters, many=True)
#         return Response(serializer.data)

#     def perform_create(self, serializer: serializers.ChapterSerialzer):
#         lookup_key = self.kwargs[self.lookup_field]
#         manga = self.queryset.filter(route=lookup_key).first()
#         serializer.save(manga=manga)
