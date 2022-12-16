from rest_framework import status, authentication, generics, filters

from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from . import models
from . import serializers

from .authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly

# Start Migrating from APIView To genericsView


class MangaGenericListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Manga.objects.all()
    serializer_class = serializers.MangaSerializer
    authentication_classes = [TokenAuthentication,
                              authentication.SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'author', "release_year", "status"]

    def get_serializer_class(self):
        params = self.request.query_params
        if len(params) != 0:
            return serializers.MangaSearchSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
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
    authentication_classes = [TokenAuthentication,
                              authentication.SessionAuthentication]

    permission_classes = [IsAdminOrReadOnly]

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
