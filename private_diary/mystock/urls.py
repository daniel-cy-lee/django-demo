from django.urls import path
from .views import StockListView, send_notification, refresh_data

app_name = "stock_app"
urlpatterns = [
    path("stock_url/", StockListView.as_view(), name="my_stock_app"),
    path('send-notification/', send_notification, name='send-notification'),
    path('refresh-data/', refresh_data, name='refresh-data'),
]

