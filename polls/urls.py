from django.urls import path
from polls import views

urlpatterns = {
    path('', views.indexpage),
    path('create/', views.create),
    path('vote/', views.vote),
    path('result/', views.result),
}