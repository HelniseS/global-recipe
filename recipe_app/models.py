from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.
User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

        class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('african', 'African'),
        ('asian', 'Asian'),
        ('european', 'European'),
        ('american', 'American'),
        ('vegan', 'Vegan'),
        ('desserts', 'Desserts'),
        ('quick', 'Quick'),
        ('other', 'Other'),
    ]

