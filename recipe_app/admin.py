from django.contrib import admin
from .models import Recipe, Ingredient, Step, Nutrition, Tag

# Register your models here.
class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0

    class StepInline(admin.TabularInline):
    model = Step
    extra = 0