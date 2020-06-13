from django.urls import path
from polls import views
from polls.views import (
    TestListView,
    TestCreateView,
    TestUpdateView,
    TestDetailView,
    TestDeleteView
)

urlpatterns = [
    path('', TestListView.as_view(), name='home'),
    path('create_test/', TestCreateView.as_view(), name='create_test'),
    path('test/<str:slug>/', TestDetailView.as_view(), name='detail_test'),
    path('test/<str:slug>/update/', TestUpdateView.as_view(), name='update_test'),
    path('test/<str:slug>/delete/', TestDeleteView.as_view(), name='delete_test'),
]