# recipe_app/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Nutrition, Ingredient, Step

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "category", "description", "cooking_time_min", "servings", "image", "rating", "tags"]

class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ["calories", "protein_g", "carbs_g", "fat_g"]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["text"]

class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ["order", "text"]

IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient, form=IngredientForm, extra=10, can_delete=True
)

StepFormSet = inlineformset_factory(
    Recipe, Step, form=StepForm, extra=1, can_delete=True
)
