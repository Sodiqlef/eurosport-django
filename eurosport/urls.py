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
    path('result/d1', views.played_d1, name="d1r"),
    path('fixtures/d1', views.upcoming_d1, name="d1f"),
    path('result/d2', views.played_d2, name="d2r"),
    path('fixtures/d2', views.upcoming_d2, name="d2f"),
    path('result/d2/cup', views.played_d2_cup, name="d2_cupr"),
    path('fixtures/d2/cup', views.upcoming_d2_cup, name="d2_cupf"),
    path('result/d1/cup', views.played_d1_cup, name="d1_cupr"),
    path('fixtures/d1/cup', views.upcoming_d1_cup, name="d1_cupf"),
    path('result/super-cup', views.played_super_cup, name="super_cupr"),
    path('fixtures/super-cup', views.upcoming_super_cup, name="super_cupf"),
    path('result/champions-league', views.played_cl, name="championr"),
    path('fixtures/champions-league', views.upcoming_cl, name="championf"),
    path('result/europa-league', views.played_el, name="europar"),
    path('fixtures/europa-league', views.upcoming_el, name="europaf"),
    path('result/international-matches', views.played_international, name="internationalr"),
    path('fixtures/international-matches', views.upcoming_international, name="internationalf"),

    re_path(r'^match/(?P<pk>\d+)/$', views.match_details, name='match_details')
]
