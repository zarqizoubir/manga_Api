from django.urls import path


from . import views

urlpatterns = [
    path("<str:id_name>/",
         views.ChapterGenericListCreateApiView.as_view()),

    path("<str:id_name>/<int:number>/",
         views.ChapterGenericsRetreiveUpdateDestroy.as_view()),

]
