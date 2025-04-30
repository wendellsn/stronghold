from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produto/<int:produto_id>/', views.produto_detail, name='produto_detail'),
    path('sortear/<int:produto_id>/', views.sortear, name='sortear'),
]
