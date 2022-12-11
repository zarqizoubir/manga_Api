from django.urls import path, re_path

from . import views


urlpatterns = [
    path("", views.MangaCreateListApiView.as_view()),
    path("test/", views.MangaGenericListCreateApiView.as_view()),
    path("<str:manga>/", views.MangaRetrieveUpdateDestroy.as_view()),
    path("<str:manga>/chapters/", views.ChapterCreateListApiView.as_view()),
    path("<str:manga>/chapters/<str:number>/",
         views.ChapterRetreiveUpdateDestroy.as_view()),
]
