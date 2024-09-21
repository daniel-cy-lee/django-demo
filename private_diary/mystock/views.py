from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class StockListView(ListView):
  model = models.StockModel
  template_name = 'stock_list.html'  # Your HTML template

