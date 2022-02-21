"""housepriceprediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from .import settings
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    
    path("predictwoji/",views.predictwoji,name="predictwoji"),
    path("predictwoji/resultwoji/",views.resultwoji,name="resultwoji"),
    
    path("predictgra/",views.predictgra,name="predictgra"),
    path("predictgra/resultgra/",views.resultgra,name="resultgra"),
    
    path("predictruk/",views.predictruk,name="predictruk"),
    path("predictruk/resultruk/",views.resultruk,name="resultruk"),

    path("predicttrans/", views.predicttrans, name="predicttrans"),
    path("predicttrans/resulttrans/", views.resulttrans, name="resulttrans"),
    
    path("predictada/",views.predictada,name="predictada"),
    path("predictada/resultada/",views.resultada,name="resultada"),

    path("predictdiobu/", views.predictdiobu, name="predictdiobu"),
    path("predictdiobu/resultdiobu/", views.resultdiobu, name="resultdiobu"),
    
    
]

