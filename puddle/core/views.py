from django.shortcuts import render, redirect
from verify_email.email_handler import send_verification_email

from item.models import Category, Item
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            #form.save()

            return redirect('/verify_page/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form':form,
    })

def verify_page(request):
    return render(request, 'core/verify.html')