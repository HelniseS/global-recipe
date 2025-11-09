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


class RecipeListView(ListView):
    template_name = "recipe_app/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 12

    def get_queryset(self):
        qs = Recipe.objects.select_related("author").prefetch_related("tags").order_by("-created_at")
        q = self.request.GET.get("q")
        tag = self.request.GET.get("tag")
        cat = self.request.GET.get("category")
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(ingredients__text__icontains=q)).distinct()
        if tag:
            qs = qs.filter(tags__name__iexact=tag)
        if cat:
            qs = qs.filter(category=cat)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["tags"] = Tag.objects.all()
        ctx["active_tag"] = self.request.GET.get("tag", "")
        ctx["active_category"] = self.request.GET.get("category", "")
        ctx["q"] = self.request.GET.get("q", "")
        return ctx
   
class RecipeDetailView(DetailView):
    template_name = "recipe_app/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"


