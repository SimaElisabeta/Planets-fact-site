from django.urls import path
from . import views

app_name = 'planets_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:planet_name>/<str:planet_section>/', views.planet_detail, name='planet_detail'),
    path('compare/', views.compare_planets, name='compare_planets'),
    path('api/v1/planets/', views.api_planet, name='api_planet'),
    path('api/', views.api_help, name='api_help')
]
