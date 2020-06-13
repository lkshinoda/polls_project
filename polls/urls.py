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
    QuestionDeleteView
)

urlpatterns = [
    path('', TestListView.as_view(), name='home'),
    path('create_test/', TestCreateView.as_view(), name='create_test'),
    path('test/<str:slug>/', TestDetailView.as_view(), name='detail_test'),
    path('test/<str:slug>/update/', TestUpdateView.as_view(), name='update_test'),
    path('test/<str:slug>/delete/', TestDeleteView.as_view(), name='delete_test'),
    path('create_question/', QuestionCreateView.as_view(), name='create_question'),
    path('question/', QuestionListView.as_view(), name='list_question'),
    path('detail_question/<int:pk>/', QuestionDetailView.as_view(), name='detail_question'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='update_question'),
    path('question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='delete_question'),
]