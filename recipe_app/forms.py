# recipe_app/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Nutrition, Ingredient, Step

class RecipeForm(forms.ModelForm):
    RATING_CHOICES =[
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES)

    class Meta:
        model = Recipe
        fields = ["title", "category", "description", "cooking_time_min", "servings", "image", "tags", "rating"]

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
    Recipe, Ingredient, form=IngredientForm, extra=15
)

StepFormSet = inlineformset_factory(
    Recipe, Step, form=StepForm, extra=15
)
