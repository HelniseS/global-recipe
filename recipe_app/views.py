# recipe_app/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from .models import Recipe, Tag
from .forms import RecipeForm, NutritionForm, IngredientFormSet, StepFormSet


class HomeView(ListView):
    template_name = "recipe_app/home.html"
    context_object_name = "recipes"
    paginate_by = 8

    def get_queryset(self):
        return Recipe.objects.select_related("author").prefetch_related("tags").order_by("-created_at")[:8]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["tags"] = Tag.objects.all()
        return ctx



