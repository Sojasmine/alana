from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def index(request):
    """
    A view to return the index page
    """
    return render(request, 'home/index.html')


def contact(request):
   
   return render(request, 'home/contact_us.html')
