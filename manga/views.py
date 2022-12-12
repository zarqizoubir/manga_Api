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

    # Default Processing using GET

    # def get(self, request, *args, **kwargs):
    #     params = request.query_params["search"] if request.GET.get(
    #         "search") != None else ""
    #     if params:
    #         serializer = serializers.MangaSearchSerializer(
    #             self.get_search_query(params), many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     serializer = self.serializer(self.get_objects(), many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        params = request.query_params["search"] if request.GET.get(
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
            if serializer.validated_data.get("poster"):
                serializer.validated_data.get(
                    "poster").name = unique_id+".png"

            id_name = unique_id
            serializer.save(id_name=id_name, endpoint=url_endpoint)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class MangaGenericsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Manga
    serializer_class = serializers.MangaSerializer
    lookup_field = "id_name"

    def perform_update(self, serializer):
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data.get('poster'))
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


# class ChapterGenericListCreateApiView(generics.ListCreateAPIView):
#     queryset = models.Manga
#     serializer_class = serializers.ChapterSerialzer

#     def get_objects(self, id_name: str):
#         try:
#             return self.queryset.objects.filter(id_name=id_name).first()
#         except models.Manga.DoesNotExist:
#             raise Http404

#     def get(self, request: HttpRequest, id_name: str):
#         chapters = self.get_objects(id_name).chapters
#         # serializer = self.serializer(chapters, many=True)
#         serializer = self.get_serializer(chapters, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request: HttpRequest, id_name: str):
#         obj = self.get_objects(id_name=id_name)
#         data = request.data
#         serializer = serializers.ChapterSerialzer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             # manga = serializer.validated_data.get("manga")
#             serializer.save(
#                 manga=obj, name=f"{id_name}_{obj.chapters.count()+1}")
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ChapterGenericsRetreiveUpdateDestroy(
#     generics.GenericAPIView,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin
# ):
#     queryset = models.Manga
#     serializer_class = serializers.ChapterSerialzer

#     def get_serializer_class(self):
#         method = self.request.method
#         if method == "POST":
#             return serializers.ChapterPartSerializer
#         return super().get_serializer_class()

#     def get_object(self, id_name: str, name: str):
#         try:
#             obj = self.get_queryset().objects.get(
#                 id_name=id_name).chapters.filter(name=name).first()
#             if obj:
#                 return obj
#             raise Http404
#         except:
#             raise Http404

#     def get(self, request: HttpRequest, id_name: str, name: int):
#         query_set = self.get_object(id_name, name)
#         serializer = self.get_serializer(query_set)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#         # return Response({}, status=status.HTTP_200_OK)

#     def post(self, request: HttpRequest, id_name: str, name: str):
#         query_set = self.get_object(id_name, name)
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title: str = serializer.validated_data.get("title")
#             if serializer.validated_data.get("image"):
#                 serializer.validated_data.get(
#                     "image").name = title.lower().replace(" ", "_")+".png"
#             serializer.save(chapter=query_set)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request: HttpRequest, id_name: str, name: str):
#         query_set = self.get_object(id_name, name)
#         serializer = self.get_serializer(query_set, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request: HttpRequest, id_name: str, name: str):
#         query_set = self.get_object(id_name, name)
#         query_set.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
