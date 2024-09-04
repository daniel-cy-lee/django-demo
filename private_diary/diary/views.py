# Create your views here.

from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
import logging
from django.urls import reverse_lazy

class IndexView(generic.TemplateView):
    template_name = "index.html"

logger = logging.getLogger(__name__)
class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy("diary:inquiry")

    def form_valid(self, form):
     	  # Handle form submission here (e.g., send email, save to database)
          form.send_email()
          logger.info("Inquiry sent by {}".format(form.cleaned_data["name"]))
          # Redirect to the success URL after processing the form
          return super().form_valid(form)

#    def get_success_url(self):
#     	  # Redirect to a success page or URL after successful form submission
#     	  #return '/success/'
#          return '/'
