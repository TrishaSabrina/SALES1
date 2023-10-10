from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.item_list),
    path('sales/<int:pk>/', views.item_detail),
]