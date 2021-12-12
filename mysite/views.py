from django.shortcuts import render, HttpResponse
from datetime import datetime
from mysite.models import post,Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    descs = post.objects.all()

    
   
    return render(request,'index.html',{"descs" : descs})
@login_required
def contact(request):
    

    if request.method == "POST":
        name = request.POST.get('name')
        email =request.POST.get('email')
        feedback =request.POST.get('feedback')
        contact = Contact(name=name,email=email,feedback=feedback)
        contact.save()
        messages.info(request,'Feedback Summited')

    return render(request,'contact.html')   

@login_required
def about(request):
    return render(request,'about.html') 
@login_required
def posts(request):
    if request.method == "POST":
        desc = request.POST.get('desc')
        img = request.POST.get('img')
        price = request.POST.get('price')
        des = post(desc=desc,img=img,price=price)
        des.save()

      
    return render(request,'posts.html') 



    



