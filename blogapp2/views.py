from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class AnswersListView(ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = 'answers_list_template.html'

class AnswerDetailView(DetailView):
    model = Answer
    context_object_name = 'answer'
    template_name = 'answer_detail_template.html'

class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'answer_create_template.html'
    fields = ['header', 'body', 'author']
    success_url = reverse_lazy('answers_list_url')
