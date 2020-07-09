from django.urls import path
from polls import views
from polls.views import (
    TestListView,
    TestCreateView,
    TestUpdateView,
    TestDetailView,
    TestDeleteView,
    
    QuestionCreateView,
    QuestionListView,
    QuestionDetailView,
    QuestionUpdateView,
    QuestionDeleteView,
    
    PollDetailView,
    PollUpdateView,
    PollDeleteView,
    
    RunTestView,
)


urlpatterns = [
    path('', views.view_poll, name='home'),
    
    path('test/', TestListView.as_view(), name='test_list'),
    path('create_test/', TestCreateView.as_view(), name='create_test'),
    path('test/<str:slug>/', TestDetailView.as_view(), name='detail_test'),
    path('test/<str:slug>/update/', TestUpdateView.as_view(), name='update_test'),
    path('test/<str:slug>/delete/', TestDeleteView.as_view(), name='delete_test'),
    path('test/<str:slug>/run/', RunTestView.as_view(), name='run_test'),
    
    path('create_question/', views.create_question, name='create_question'),
    path('question/', QuestionListView.as_view(), name='list_question'),
    path('detail_question/<int:pk>/', QuestionDetailView.as_view(), name='detail_question'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='update_question'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='delete_question'),
    
    path('poll/<str:slug>/', PollDetailView.as_view(), name='detail_poll'),
    path('poll/<str:slug>/update/', PollUpdateView.as_view(), name='update_poll'),
    path('poll/<str:slug>/delete/', PollDeleteView.as_view(), name='delete_poll'),
]