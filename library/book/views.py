from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

def index(request):
    shelf = Book.objects.all()
    return render(request, 'library.html',{'shelf': shelf}) 

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index') 
        else:
            return HttpResponse(""" Something went wrong. Wait for a minute """)
    else:
        return render(request, 'upload_form.html', {'upload_form': upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    
    if request.method == 'POST':
        book_form = BookCreate(request.POST, request.FILES, instance=book_shelf)
        if book_form.is_valid():
            book_form.save()
            return redirect('index')
    else:
        book_form = BookCreate(instance=book_shelf)
    
    return render(request, 'upload_form.html', {'upload_form': book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_shelf.delete()
    return redirect('index')    

    

