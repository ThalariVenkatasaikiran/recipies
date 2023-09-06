from django.db import models

# Create your models here.
# from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    process = models.TextField()
    recipe_images = models.ImageField(upload_to='recipe_images/')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Use Django's built-in password hashing
    profile_pic = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.username
