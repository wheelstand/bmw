from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Trim, Models, ModelsShown


class TrimList(ListView):
    model = Trim


class TrimDetail(DetailView):
    model = Trim











