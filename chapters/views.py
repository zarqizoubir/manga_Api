from django.http import Http404

from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.request import HttpRequest
from rest_framework.response import Response


from . import serializers
from manga import models


class ChapterGenericListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Manga
    serializer_class = serializers.ChapterSerialzer

    def get_objects(self, id_name: str):
        try:
            return self.queryset.objects.filter(id_name=id_name).first()
        except models.Manga.DoesNotExist:
            raise Http404

    def get(self, request: HttpRequest, id_name: str):
        chapters = self.get_objects(id_name).chapters
        # serializer = self.serializer(chapters, many=True)
        serializer = self.get_serializer(chapters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest, id_name: str):
        obj = self.get_objects(id_name=id_name)
        data = request.data
        serializer = serializers.ChapterSerialzer(data=data)
        if serializer.is_valid(raise_exception=True):
            # manga = serializer.validated_data.get("manga")
            serializer.save(
                manga=obj, name=f"{id_name}_{obj.chapters.count()+1}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChapterGenericsRetreiveUpdateDestroy(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = models.Manga
    serializer_class = serializers.ChapterSerialzer

    def get_serializer_class(self):
        method = self.request.method
        if method == "POST":
            return serializers.ChapterPartSerializer
        return super().get_serializer_class()

    def get_object(self, id_name: str, name: str):
        try:
            obj = self.get_queryset().objects.get(
                id_name=id_name).chapters.filter(name=name).first()
            if obj:
                return obj
            raise Http404
        except:
            raise Http404

    def get(self, request: HttpRequest, id_name: str, number: int):
        name = f"{id_name}_{number}"
        query_set = self.get_object(id_name, name)
        serializer = self.get_serializer(query_set)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response({}, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest, id_name: str, number: int):
        name = f"{id_name}_{number}"
        query_set = self.get_object(id_name, name)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title: str = serializer.validated_data.get("title")
            if serializer.validated_data.get("image"):
                serializer.validated_data.get(
                    "image").name = title.lower().replace(" ", "_")+".png"
            serializer.save(chapter=query_set)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: HttpRequest, id_name: str, number: int):
        name = f"{id_name}_{number}"
        query_set = self.get_object(id_name, name)
        serializer = self.get_serializer(query_set, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, id_name: str, name: str):
        query_set = self.get_object(id_name, name)
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
