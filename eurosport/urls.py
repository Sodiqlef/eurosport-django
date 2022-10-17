"""eurosport URL Configuration

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
from django.urls import path, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('transfer/', views.transfer, name="transfer"),
    path('news/', views.news, name="news"),
    path('standings/', views.standings, name="standings"),
    path('result/', views.played_matches, name="played"),
    path('fixtures/', views.upcoming_matches, name="upcoming"),
    re_path(r'^match/(?P<pk>\d+)/$', views.match_details, name='match_details')
]
