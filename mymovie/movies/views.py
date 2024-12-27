from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
# Create your views here.


def registerPage(request):
    form = CreateUserForm()
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+username)
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'movies/register.html', context)

def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'movies/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login') 

def home(request):
    context = {}
    objs = Movie.objects.all()
    context['objs'] = objs
    return render(request, 'movies/home.html', context)

def addmovies(request):
    context = {}
    form = MovieForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'movies/addmovies.html', context)

def search(request):
    query = request.GET['query']
    objs = Movie.objects.filter(movie_name__icontains=query)
    context = {'objs':objs}
    return render(request, 'movies/search.html', context)

def detailPage(request, pk):
    context = {}
    obj = Movie.objects.get(id=pk)
    context['obj'] = obj
    return render(request, 'movies/detail.html', context)
