from django.db import models


'''
class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
            """Returns the url to access a particular instance of MyModelName."""
            return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.field_name
'''
# Create your models here.
class StockModel(models.Model):
    stock_id = models.CharField(
        max_length=10,
        unique=True,
        help_text="stock id ex:00679B"
    )

    name = models.CharField(max_length=20, help_text='Stock name, ex 元大美債20年')

    bid_price = models.FloatField(help_text='bid price')
    price_chage_ratio = models.FloatField(help_text='price chage ratio in %')
    ask_price_first = models.FloatField(help_text='ask (sell) price data 1')
    ask_price_last = models.FloatField(help_text='ask (sell) price data 5')

    buy_price_first = models.FloatField(help_text='buy price data 1')
    buy_price_last = models.FloatField(help_text='buy price data 5')

    open_price = models.FloatField(help_text='open price')

    date_time = models.DateTimeField()
