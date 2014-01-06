#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from books.models import Book
from django.core.mail import send_mail
from forms import ContactForm

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
 
'''
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):#get subject的值 默认为''
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email','noreply@example.com'),
                ['siteowner@example.com'],
                )
            return HttpResponseRedirect('/contact/thanks/')
    return render(request,'contact_form.html',{
        'errors':errors,
        'subject':request.POST.get('subject',''),
        'message':request.POST.get('message',''),
        'email':request.POST.get('email',''),}
        )
'''

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['siteowner@example.com'],
                )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':'I love your site!'} 
        )
    return render(request,'contact_form.html',{'form':form})

def thanks(request):
    return HttpResponse("Thanks for your Post!")

def tags(request):
    words = "hello vose, good morning, it's a good day is't it ?"
    return render(request,'tags.html',{'words':words})
