from django.urls import path
from polls import views

urlpatterns = [
    path('', views.indexpage, name='home'),
    path('create_test/', views.create_test, name='create_test'),
    path('update/<str:pk>/', views.update_test, name='update_test'),
    path('test/<str:slug>/', views.test_view, name='test')
]