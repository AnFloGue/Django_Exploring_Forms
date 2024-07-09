from django.shortcuts import render
from .models import Author
from .models import ContactFormLog


def home(request):
    """
    Handles the request to the home page of the website.

    Args:
        The request object.

    Returns:
        The response object, which renders the index page.
    """
    
    obj_list = ContactFormLog.objects.all()
    name = "Antonio"
    age = 55
    return render(request, 'home.html', {'data': obj_list, 'name': name, 'age': age})


def index(request):
    """
    Handles the request to the index page of the website.

    Args:
        The request object.

    Returns:
        The response object, which renders the index page.
    """
    obj_list = ContactFormLog.objects.all()
    return render(request, 'index.html', {"data": obj_list})

def addnew(request):
    return render(request, 'addnew.html')