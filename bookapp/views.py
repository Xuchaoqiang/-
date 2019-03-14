from django.shortcuts import render

# Create your views here.

def books(request):


    return render(request, "books.html")

def addbook(request):

    return render(request, "addbook.html")
