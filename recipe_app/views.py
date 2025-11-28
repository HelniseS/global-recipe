# recipe_app/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, UpdateView, DeleteView
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

class RecipeCreateView(LoginRequiredMixin, View):
    template_name = "recipe_app/recipe_form.html"
    success_url = reverse_lazy("recipe_app:recipe_list")

    def get(self, request):
        form = RecipeForm()
        nutrition_form = NutritionForm()
        ingredient_formset = IngredientFormSet()
        step_formset = StepFormSet()

        return render(request, self.template_name, {
            "form": form,
            "nutrition_form": nutrition_form,
            "ingredient_formset": ingredient_formset,
            "step_formset": step_formset,
        })

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        nutrition_form = NutritionForm(request.POST)
        ingredient_formset = IngredientFormSet(request.POST)
        step_formset = StepFormSet(request.POST)

        if (form.is_valid() and nutrition_form.is_valid()
                and ingredient_formset.is_valid() and step_formset.is_valid()):

            # Save main recipe
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            # Save nutrition info
            nutrition = nutrition_form.save(commit=False)
            nutrition.recipe = recipe
            nutrition.save()

            # Save ingredients
            ingredients = ingredient_formset.save(commit=False)
            for ing in ingredients:
                ing.recipe = recipe
                ing.save()
            for obj in ingredient_formset.deleted_objects:
                obj.delete()

            # Save steps
            steps = step_formset.save(commit=False)
            for step in steps:
                step.recipe = recipe
                step.save()
            for obj in step_formset.deleted_objects:
                obj.delete()

            return redirect(self.success_url)

        # If anything is invalid, show the form again with errors
        return render(request, self.template_name, {
            "form": form,
            "nutrition_form": nutrition_form,
            "ingredient_formset": ingredient_formset,
            "step_formset": step_formset,
        })


class MyRecipesView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipe_app/my_recipes.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user).order_by("-created_at")


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    template_name = "recipe_app/recipe_form.html"
    fields = ["title", "image", "category", "description",
              "cooking_time_min", "servings", "rating"]

    def test_func(self):
        return self.get_object().author == self.request.user


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "recipe_app/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe_app:recipe_list")

    def test_func(self):
        return self.get_object().author == self.request.user

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")