
from django.urls import path
from . import views


urlpatterns = [
    path('', views.batman, name="batman"),
    path('<int:hero_id>/', views.hero_detail, name="hero-detail"),
]
