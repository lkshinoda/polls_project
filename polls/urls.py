from django.urls import path
from polls import views

urlpatterns = [
    path('', views.indexpage, name='home'),
    path('create/', views.create, name='create'),
    path('update/<str:pk>/', views.update, name='update'),
]