from django.urls import path

from . import views


urlpatterns = [
    path("", views.MangaListCreateApiView.as_view()),
    path("<str:route>/", views.MangaUpdateDestroyApiView.as_view()),
    path("<str:route>/chapters/", views.ChapterListCreate.as_view()),
]
