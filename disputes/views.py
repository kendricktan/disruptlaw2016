from django.shortcuts import render, HttpResponse
from django.core.validators import validate_email

def index_view(request):
    return render(request, 'index.html', {})

def landing(request):
    if request.method == "POST":
        email = request.POST['email']
        validate_email(email)

        return HttpResponse('yay')

    return render(request, 'landing.html', {})

def resolve(request):
    return render(request, 'resolve.html', {})

def dispute(request):
    return render(request, 'dispute.html', {})