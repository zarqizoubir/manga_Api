from django.urls import path, re_path

from . import views


urlpatterns = [
    path("", views.MangaGenericListCreateApiView.as_view()),

    path("<str:id_name>/", views.MangaGenericsRetrieveUpdateDestroy.as_view()),

    path("<str:manga>/chapters/", views.ChapterCreateListApiView.as_view()),
    path("<str:manga>/chapters/<str:number>/",
         views.ChapterRetreiveUpdateDestroy.as_view()),
]
