from django.shortcuts import render
from django.http import HttpResponse
from . import views



def admin_console(request):

    return render(request, 'products/products_page.html')
