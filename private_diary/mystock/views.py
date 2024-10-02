from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import StockModel
from . import stock_query


# Create your views here.
class StockListView(ListView):
  model = StockModel
  #context_object_name = 'my_book_list'   # your own name for the list as a template variable
  template_name = 'stock_list.html'  # Your HTML template

  def get_queryset(self):
    # get data
    # stock_query.py
    stocks_data = stock_query.query()
    # stock_query.stock_2_line()
    for stock_data in stocks_data:
      StockModel.objects.update_or_create(
        stock_id=stock_data.stock_id,
        defaults={
            'name': stock_data.name,
            'bid_price': stock_data.bid,
            'price_chage_ratio': stock_data.cratio,
            'ask_price_first': float(stock_data.ask_list[0]),
            'ask_price_last': float(stock_data.ask_list[-1]),
            'buy_price_first': float(stock_data.buy_list[0]),
            'buy_price_last': float(stock_data.buy_list[-1]),
            'high_price': stock_data.high,
            'low_price': stock_data.low,
            'open_price': stock_data.open,
            'date_time': stock_data.time_str,
        }
    )
    # Return the updated list of books from the database
    return StockModel.objects.all()

# Action for sending Line notification (triggered by the first button)
def send_notification(request):
    stock_query.stock_2_line()
    return redirect('stock_app:my_stock_app')  # Redirect back to the stock list after the action


# Action for refreshing stock data (triggered by the second button)
def refresh_data(request):
    stocks_data = stock_query.query()
    for stock_data in stocks_data:
        StockModel.objects.update_or_create(
            stock_id=stock_data.stock_id,
            defaults={
                'name': stock_data.name,
                'bid_price': stock_data.bid,
                'price_chage_ratio': stock_data.cratio,
                'ask_price_first': float(stock_data.ask_list[0]),
                'ask_price_last': float(stock_data.ask_list[-1]),
                'buy_price_first': float(stock_data.buy_list[0]),
                'buy_price_last': float(stock_data.buy_list[-1]),
                'high_price': stock_data.high,
                'low_price': stock_data.low,
                'open_price': stock_data.open,
                'date_time': stock_data.time_str,
            }
        )
    return redirect('stock_app:my_stock_app')  # Redirect back to the stock list after the action
