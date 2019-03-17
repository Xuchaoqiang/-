from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bookapp.models import *

# Create your views here.

@csrf_exempt
def books(request):

    if request.method == 'POST':
        did = request.POST.get('did')
        print(did)
        Book.objects.filter(id=did).delete()
    book_list = Book.objects.all()

    return render(request, "books.html", locals())

@csrf_exempt
def addbook(request):
    if request.method == "POST":
        data = request.POST
        book_obj = Book.objects.create(
            title=(data.get('title')),
            price=(data.get('price')),
            pub_date=(data.get('pub_date')),
            publish_id=(data.get('publish_id'))
        )
        author_list = data.getlist('author_list')
        book_obj.authors.add(*author_list)

        return redirect("/books/")
    else:
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request, "addbook.html", {"publish_list": publish_list, "author_list": author_list})


@csrf_exempt
def change(request, id):
    book_obj = Book.objects.filter(id=id).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        author_list = request.POST.getlist('author_list')

        print(author_list)

        Book.objects.filter(pk=id).update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)

        # book_obj.authors.clear()
        # book_obj.authors.add(*author_list)
        book_obj.authors.set(author_list)

        return redirect("/books/")
    else:
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request, "change.html", {"publish_list": publish_list, "author_list": author_list, "book_obj": book_obj})

def delbook(request, id):
    Book.objects.filter(id=id).delete()
    return redirect("/books/")