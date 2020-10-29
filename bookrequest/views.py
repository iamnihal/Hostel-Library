from django.shortcuts import render, redirect
from .forms import BookRequestForm
from django.contrib import messages
from .models import BookRequest

def book_request(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('requested-books')
    else:
        form = BookRequestForm()
    return render(request, 'bookrequest/request.html', {'form':form})

def requested_index(request):
    requested = BookRequest.objects.order_by('-date_posted')
    context = {
        'requested':requested
    }
    return render(request, 'bookrequest/request_books.html', context)
            
        
