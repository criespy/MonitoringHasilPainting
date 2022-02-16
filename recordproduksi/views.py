from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from app_settings import ADMINLTE_URL

from .models import RencanaProduksi, RencanaProduksiDetail

class HompageView(ListView):
    model = RencanaProduksi
    template_name = 'index.html'