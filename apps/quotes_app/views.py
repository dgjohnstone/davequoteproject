from django.shortcuts import render, redirect
from models import User, Quote
from django.contrib import messages
# Create your views here.

def dashboard(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'quotes': Quote.objects.all(),
        
        
    }
    return render(request, 'quotes_app/dashboard.html', context)



def add(request):
    
        x =  Quote.objects.create(name = request.POST['person'], message = request.POST['message'], creator= User.objects.get(id=request.session['id']))
        return redirect('/main/dashboard')

def show(request, id):
    context = {
        'user':User.objects.get(id=request.session['id']),
        'quotes': Quote.objects.filter(creator__id=id),
        'count ': Quote.objects.count()
    }
    
    return render(request,'quotes_app/show.html', context)

def favorite(request, id):
    Quote.objects.get(id = id).favorite.add(User.objects.get(id=request.session['id'])),
    return redirect('/main/dashboard')
