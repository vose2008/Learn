#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# Create your views here.
#def search_form(request):
    #return render(request,'search_form.html')

#The bad example
'''
def search(request):
    errors = []
    if 'q' in request.GET:
        if request.GET['q']:
            q = request.GET['q']
            if len(q) > 20:
                errors.append("Please submit a search term 20 characters or shorter.")
                
            else:
                books = Book.objects.filter(title__icontains=q)
                return render(request,'search_results.html',{'books':books,'query':q})
        else:
            errors.append("You submitted an empty form.")
    else:
        pass
    return render(request,'search_form.html',{'errors':errors})
'''
#The good
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Enter a search term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters.")
        else:
            books = Book.objects.filter(title__icontains=q)
            #title__icontaings=q 获取数据库中标题包含q的书籍
            return render(request,'search_results.html',{'books':books,'query':q})
    return render(request,'search_form.html',{'errors':errors})
        
