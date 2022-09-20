"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main, name='main'),

    path('player/', views.listPlayer, name='player'),
    path('registerPlayer/', views.registerPlayer, name='registerPlayer'),
    path('editPlayer/<int:id>', views.editPlayer, name='editPlayer'),
    path('deletePlayer/<int:id>', views.deletePlayer, name='deletePlayer'),
    path('updatePlayer/<int:id>', views.updatePlayer, name='updatePlayer'),

    path('team/', views.listTeam, name='team'),
    path('registerTeam/', views.registerTeam, name='registerTeam'),
    path('editTeam/<int:id>', views.editTeam, name='editTeam'),
    path('deleteTeam/<int:id>', views.deleteTeam, name='deleteTeam'),
    path('updateTeam/<int:id>', views.updateTeam, name='updateTeam'),

    path('stadium/', views.listStadium, name='stadium'),
    path('registerStadium/', views.registerStadium, name='registerStadium'),
    path('editStadium/<int:id>', views.editStadium, name='editStadium'),
    path('deleteStadium/<int:id>', views.deleteStadium, name='deleteStadium'),
    path('updateStadium/<int:id>', views.updateStadium, name='updateStadium'),
]