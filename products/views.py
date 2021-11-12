from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.


def LoginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('products')

    
    return render(request,'login_register.html',{'page':page})

def LogoutUser(request):
    logout(request) 
    return redirect('login')

def registeruser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request,username=user.username,password=request.POST['password1'])
            if user is not None:
                login(request,user)
                return redirect('products')

    context = {'form' : form, 'page':page}
    return render(request,'login_register.html',context)

@login_required(login_url='login')
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{
        'products': products
    })


def new(request):
    return  HttpResponse('products page')

