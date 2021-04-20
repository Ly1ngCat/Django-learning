from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "home.html", {})
    

def contacts_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contacts Page</h1>")    
    return render(request, "contacts.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": 123,
        "my_list": [213,312,55555, "Abc"]
    }

    #return HttpResponse("<h1>About Page</h1>")    
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Social Page</h1>")    
    return render(request, "social.html", {})
