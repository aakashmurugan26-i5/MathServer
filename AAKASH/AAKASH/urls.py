
from django.contrib import admin
from django.urls import path
from AAKA import views

urlpatterns = [
    path('', views.cumChurn_Rate_area, name='cumChurn_Rate_area'),
]