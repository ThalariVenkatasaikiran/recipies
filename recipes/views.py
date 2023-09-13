# from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import RecipeForm, LoginForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RegistrationForm

# ...


def user_login(request):
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes')
    else:
        form = LoginForm()
    return render(request, 'recipes/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # username = form.cleaned_data['username']
            import pdb;pdb.set_trace()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # date_of_birth = form.cleaned_data['date_of_birth']
            profile_pic = form.cleaned_data['profile_pic']
            # # Create the user
            user = MyUser.objects.create_user(email=email,
                                              password=password,
                                              # date_of_birth=date_of_birth,
                                              profile_pic=profile_pic)
            user.save()
            # Log the user in
            user = authenticate(request, email=email, password=password)
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


def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_details.html', {'recipe': recipe})


def user_logout(request):
    logout(request)
    return redirect('login')
