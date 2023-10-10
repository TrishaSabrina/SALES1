from django.urls import path
from . import views

urlpatterns = [
    path('productso/', views.item_list),
    path('productso/<int:pk>/', views.item_detail),
]