from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class StockListView(ListView):
  model = models.StockModel
  template_name = 'stock_list.html'  # Your HTML template

  def get_queryset(self):
    # get data
    # stock_query.py

    '''
    for book_data in books_data:
                # Assuming the book_data contains fields like 'title', 'author', 'summary', 'isbn'
                title = book_data.get('title')
                author_name = book_data.get('author')  # Assuming the author is a simple name
                summary = book_data.get('summary')
                isbn = book_data.get('isbn')

                # Find or create the author (assuming Author model has a name field)
                author, created = Author.objects.get_or_create(name=author_name)

                # Find or create the book
                Book.objects.update_or_create(
                    isbn=isbn,
                    defaults={
                        'title': title,
                        'author': author,
                        'summary': summary
                    }
                )
    '''
    # Return the updated list of books from the database
    return models.StockModel.objects.all()
