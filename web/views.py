
from django.shortcuts import render


from .models import contact
from django.http import HttpResponse



# Create your views here.

def home (request):
    
    
    if request.method=="POST":
        Contact=contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        Contact.name=name
        Contact.email=email
        Contact.message=message
        
        Contact.save()
        return HttpResponse("<h1> Thanks  For Contact Us </h1>")
        
        
        
            
    
    return render(request,'monteblackweb/index.html')





