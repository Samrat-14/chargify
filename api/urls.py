from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('gps/', views.getGpss),
    path('gps/create/', views.createGps),
    path('gps/<str:pk>/update/', views.updateGps),
    path('gps/<str:pk>/delete/', views.deleteGps),
    path('gps/<str:pk>/', views.getGps),
]