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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("manga/", include("manga.urls")),
    path("register/", views.RegisterUser.as_view()),
    path("token/", obtain_auth_token),
    path(r'docs/', include_docs_urls(title='Polls API')),
    # path(r'docs-swagger/', schema_view),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
