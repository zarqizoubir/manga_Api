from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from .models import Manga
from . import serializers


class MangaCreateListApiView(APIView):
    model = Manga.objects.all()
    serializer = serializers.MangaSerializer

    def get(self, request: HttpRequest):
        serializer = self.serializer(self.model, many=True)
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
    model = Manga
    serializer = serializers.MangaSerializer
    lookup_key = "id_name"

    def get_object(self, manga: str):
        try:
            return self.model.objects.get(id_name=manga)
        except Manga.DoesNotExist:
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
