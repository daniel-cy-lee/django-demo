from django.shortcuts import render
from django.views.generic import ListView
from . import models
from . import stock_query

# Create your views here.
class StockListView(ListView):
  model = models.StockModel
  template_name = 'stock_list.html'  # Your HTML template

  def get_queryset(self):
    # get data
    # stock_query.py
    stocks_data = stock_query.query()

    models.StockModel.objects.update_or_create(
        stock_id=stock_data.stock_id,
        defaults={
            'name': stock_data.name,
            'bid_price': stock_data.bid,
            'price_chage_ratio': stock_data.cratio,
            'ask_price_first': float(stock_data.ask_list[0]),
            'ask_price_last': float(stock_data.ask_list[-1]),
            'buy_price_first': float(stock_data.buy_list[0]),
            'buy_price_last': float(stock_data.buy_list[-1]),
            'open_price': stock_data.open,
            'date_time': stock_data.time_int,
        }
    )
    # Return the updated list of books from the database
    return models.StockModel.objects.all()
