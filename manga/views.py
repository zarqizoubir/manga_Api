from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from . import models
from . import serializers


class MangaCreateListApiView(APIView):
    model = models.Manga
    serializer = serializers.MangaSerializer

    def get_objects(self):
        return self.model.objects.all()

    def get(self, request: HttpRequest):
        serializer = self.serializer(self.get_objects(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest):
        HOST = request.META["HTTP_HOST"]
        data = request.data
        serializer = self.serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            name: str = serializer.validated_data.get("name")
            id_name = serializer.validated_data.get("id_name")
            unique_id = name.lower().replace(" ", "_")
            if serializer.validated_data.get("poster"):
                serializer.validated_data.get(
                    "poster").name = unique_id+".png"
                print(serializer.validated_data.get("poster"))
            id_name = unique_id
            serializer.save(id_name=id_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class MangaRetrieveUpdateDestroy(APIView):
    model = models.Manga
    serializer = serializers.MangaSerializer
    lookup_key = "id_name"

    def get_object(self, manga: str):
        try:
            return self.model.objects.get(id_name=manga)
        except models.Manga.DoesNotExist:
            raise Http404

    def get(self, request: HttpRequest, manga: str):
        query_set = self.get_object(manga)
        serializer = self.serializer(query_set)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, manga: str):
        query_set = self.get_object(manga)
        serializer = self.serializer(query_set, data=request.data)
        if serializer.is_valid(raise_exception=True):
            name: str = serializer.validated_data.get("name")
            id_name = serializer.validated_data.get("id_name")
            unique_id = name.lower().replace(" ", "_")
            if serializer.validated_data.get("poster"):
                serializer.validated_data.get(
                    "poster").name = unique_id+".png"
                print(serializer.validated_data.get("poster"))
            id_name = unique_id
            serializer.save(id_name=id_name)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, manga: str):
        queryset = self.get_object(manga)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChapterCreateListApiView(APIView):
    model = models.Manga
    serializer = serializers.ChapterSerialzer

    def get_objects(self, manga: str):
        try:
            return self.model.objects.filter(id_name=manga).first()
        except models.Manga.DoesNotExist:
            raise Http404

    def get(self, request: HttpRequest, manga: str):
        chapters = self.get_objects(manga).chapters
        serializer = self.serializer(chapters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest, manga: str):
        data = request.data
        serializer = serializers.ChapterSerialzer(data=data)
        if serializer.is_valid(raise_exception=True):
            # manga = serializer.validated_data.get("manga")
            serializer.save(manga=self.get_objects(manga))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChapterRetreiveUpdateDestroy(APIView):
    model = models.Manga
    serializer = serializers.ChapterSerialzer

    def get_object(self, manga: str, number: str):
        number = float(number)
        try:
            obj = self.model.objects.get(
                id_name=manga).chapters.filter(number=number).first()
            if obj:
                return obj
            raise Http404
        except:
            raise Http404

    def get(self, request: HttpRequest, manga: str, number: str):
        query_set = self.get_object(manga, number)
        serializer = self.serializer(query_set)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpRequest, manga: str, number: str):
        query_set = self.get_object(manga, number)
        serializer = self.serializer(query_set, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, manga: str, number: str):
        query_set = self.get_object(manga, number)
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
