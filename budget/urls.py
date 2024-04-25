from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views
from .views import ThresholdViewSet

urlpatterns = [
    path('threshold/', views.ThresholdViewSet.as_view({'get': 'list', 'post': 'create'}), name='threshold'),
    path('transaction/', views.TransactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='transaction'),
    path('alert/', views.AlertViewSet.as_view({'get': 'list'}), name='alert'),
    # path('threshold-type', views.ThresholdTypeView.as_view()),
    # path('threshold', views.ThresholdViewSet.as_view()),
    # path('transaction-category', views.TransactionCategoryView.as_view()),
    # path('transaction-type', views.TransactionTypeView.as_view()),
]