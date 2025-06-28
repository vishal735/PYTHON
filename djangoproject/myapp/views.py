from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request,'index.html',{'title':'home'})

def about(request):
  return render(request,'about.html',{'title':'about'})

def blogdetails(request):
  return render(request,'blogdetails.html',{'title':'blogdetails'})

def blog(request):
   return render(request,'blog.html',{'title':'blog'})
 
def checkout(request):
   return render(request,'checkout.html',{'title':'checkout'})
 
def shop(request):
   return render(request,'shop.html',{'title':'shop'})

def shopdetails(request):
   return render(request,'shopdetails.html',{'title':'shopdetails'})
 
def shoppingcart(request):
   return render(request,'shoppingcart.html',{'title':'shoppingcart'})

def contact(request):
   return render(request,'contact.html',{'title':'contact'})
