from django.urls import path
from .views import *


urlpatterns = [
    path('answers', AnswersListView.as_view(), name='answers_list_url'),
    path('answer/<int:pk>', AnswerDetailView.as_view(), name='answer_detail_url'),
    path('answer/create', AnswerCreateView.as_view(), name='answer_create_url'),

]