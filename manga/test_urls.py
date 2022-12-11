from django.urls import path, re_path

from . import views


urlpatterns = [
    path("", views.MangaGenericListCreateApiView.as_view()),

    path("<str:id_name>/", views.MangaGenericsRetrieveUpdateDestroy.as_view()),

    path("<str:id_name>/chapters/",
         views.ChapterGenericListCreateApiView.as_view()),

    path("<str:id_name>/chapters/<str:name>/",
         views.ChapterGenericsRetreiveUpdateDestroy.as_view()),
]
