# Create your views here.

from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm

#    def form_valid(self, form):
#     	  # Handle form submission here (e.g., send email, save to database)
#          form.send_email()
#          # Redirect to the success URL after processing the form
#          return super().form_valid(form)
#          #return "123"
#
#    def get_success_url(self):
#     	  # Redirect to a success page or URL after successful form submission
#     	  #return '/success/'
#          return '/'
