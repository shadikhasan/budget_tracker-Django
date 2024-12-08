# budget/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_budget, name='main_budget'),
    path('reports/', views.reports, name='reports'),
]
