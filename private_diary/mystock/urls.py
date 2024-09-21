from django.urls import path
from . import views

app_name = "stock_app"
urlpatterns = [
    path("stock_url/", views.StockListView.as_view(), name="my_stock_app"),
]

