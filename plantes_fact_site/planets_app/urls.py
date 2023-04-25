from django.urls import path
from . import views

app_name = 'planets_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:planet_name>/<str:planet_section>/', views.planet_detail, name='planet_detail'),
    path('compare/', views.compare_planets, name='compare_planets')
]
