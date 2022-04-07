"""pypi_indexer URL Configuration

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

from django.urls import path

from pypi_app.views import SearchApiView, SearchView, DashboardView
from pypi_indexer.settings import ADMIN_ENABLED

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", DashboardView.as_view()),
    path('search/', SearchView.as_view()),
    path("api/", SearchApiView.as_view()),
]

if ADMIN_ENABLED:
    from django.contrib import admin

    urlpatterns.append(path("admin/", admin.site.urls))
