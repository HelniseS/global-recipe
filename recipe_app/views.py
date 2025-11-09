# recipe_app/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from .models import Recipe, Tag
from .forms import RecipeForm, NutritionForm, IngredientFormSet, StepFormSet


