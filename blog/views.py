from django.shortcuts import render
from .models import Contact


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
    return render(request, 'contact.html')


def shop(request):

    return render(request, 'shop.html')


def shopsingle(request):
    return render(request, 'shop-single.html')