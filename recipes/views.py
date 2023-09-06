from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import RecipeForm, LoginForm
from django.contrib.auth.models import User

# recipes/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm

# ...

def user_login(request):
    if request.method == 'POST':
        if 'register' in request.POST:  # Check if the "Register" button was clicked
            return redirect('register')  # Redirect to the registration page
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes')
    else:
        form = LoginForm()
    return render(request, 'recipes/login.html', {'form': form})


# recipes/views.py

from django.shortcuts import render, redirect
from .forms import RegistrationForm

# ...

# def register(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Handle user registration and create a new user
#             # You can access form fields like form.cleaned_data['username'], form.cleaned_data['email'], etc.
#             # Create the user, save it, and redirect to a success page or login page
#             return redirect('login')  # Redirect to the login page after registration
#     else:
#         form = RegistrationForm()
#     return render(request, 'recipes/registration.html', {'form': form})

# recipes/views.py

from django.contrib.auth import authenticate, login

# ...

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            profile_pic = form.cleaned_data['profile_pic']

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Log the user in
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'recipes/registration.html', {'form': form})



@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

from django.shortcuts import render, get_object_or_404
from .models import Recipe

def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_details.html', {'recipe': recipe})

def user_logout(request):
    logout(request)
    return redirect('login')
