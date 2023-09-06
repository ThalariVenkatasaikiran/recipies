from django.urls import path
from . import views

# app_name = "recipes"
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('recipes/', views.recipe_list, name='recipes'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('recipes/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
]

