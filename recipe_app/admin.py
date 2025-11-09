from django.contrib import admin
from .models import Recipe, Tag, Ingredient, Step, Nutrition


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0


class StepInline(admin.TabularInline):
    model = Step
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "created_at")
    list_filter = ("category", "tags")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [IngredientInline, StepInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ("recipe", "calories", "protein_g", "carbs_g", "fat_g")
