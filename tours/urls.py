from django.urls import path
from . import views

handler404 = views.custom_handler404


urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('departure/', views.DepartureView.as_view(), name='departure'),
    path('departure/<str:departure>/', views.DepartureView.as_view(), name='departure'),
    path('tour/', views.TourView.as_view(), name='tour'),
    path('tour/<int:tour_id>/', views.TourView.as_view(), name='tour'),

]
