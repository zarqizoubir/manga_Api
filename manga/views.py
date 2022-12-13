from django.http import Http404
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from . import models
from . import serializers


# Start Migrating from APIView To genericsView

class MangaGenericListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Manga.objects.all()
    serializer_class = serializers.MangaSerializer

    def get_search_query(self, params):
        return self.get_queryset().filter(
            Q(id_name__icontains=params) |
            Q(name__icontains=params) |
            Q(description__icontains=params)
        ).all()

    def get_serializer_class(self):
        params = self.request.query_params["search"] if self.request.GET.get(
            "search") != None else ""
        if params:
            return serializers.MangaSearchSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        params = self.request.query_params["search"] if self.request.GET.get(
            "search") != None else ""
        if params:
            queryset = self.get_search_query(params)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            name: str = serializer.validated_data.get("name")
            id_name = serializer.validated_data.get("id_name")
            unique_id = name.lower().replace(" ", "_")
            url_endpoint = f"{self.request.build_absolute_uri()}{unique_id}/"
            chapters_end = f"{self.request.build_absolute_uri('/')}/chapters/{unique_id}"
            if serializer.validated_data.get("poster"):
                serializer.validated_data.get(
                    "poster").name = unique_id+".png"

            id_name = unique_id
            serializer.save(id_name=id_name,
                            endpoint=url_endpoint, chapters_endpoint=chapters_end)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class MangaGenericsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Manga
    serializer_class = serializers.MangaSerializer
    lookup_field = "id_name"

    def perform_update(self, serializer: serializers.MangaSerializer):
        if serializer.is_valid(raise_exception=True):

            name: str = serializer.validated_data.get("name")
            id_name = serializer.validated_data.get("id_name")
            unique_id = name.lower().replace(" ", "_")
            url_endpoint = f"{self.request.build_absolute_uri()}{unique_id}/"
            if serializer.validated_data.get("poster"):
                serializer.validated_data.get(
                    "poster").name = unique_id+".png"

            id_name = unique_id
            serializer.save(id_name=id_name, endpoint=url_endpoint)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
