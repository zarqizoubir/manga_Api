"""omiku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Manga API",
        default_version="0.0.1",
        description="API documentation for app",
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("manga/", include("manga.urls")),
    path("chapters/", include("chapters.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path("register/", views.RegisterUser.as_view()),
    path("token/", obtain_auth_token),
    # path(r'docs/', include_docs_urls(title='Polls API', public=True)),
    path("docs/", schema_view.with_ui("redoc",
         cache_timeout=0), name="redoc-schema")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
