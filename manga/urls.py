from django.urls import path

from . import views


urlpatterns = [
    path("", views.MangaCreateListApiView.as_view()),
    path("<str:manga>/", views.MangaRetrieveUpdateDestroy.as_view()),
]
