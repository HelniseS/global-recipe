from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("african", "African"),
        ("asian", "Asian"),
        ("european", "European"),
        ("american", "American"),
        ("vegan", "Vegan"),
        ("desserts", "Desserts"),
        ("quick", "Quick"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")
    description = models.TextField(blank=True)
    cooking_time_min = models.PositiveIntegerField(default=0)
    servings = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to="recipe_images/", blank=True, null=True)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = (slugify(self.title) or "recipe")[:60]
            candidate = base
            i = 1
            while Recipe.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{i}"
                i += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("recipe_app:recipe_detail", args=[self.pk])


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    text = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return self.text


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")
    order = models.PositiveIntegerField()
    text = models.TextField()

    class Meta:
        ordering = ["order"]
        unique_together = ("recipe", "order")

    def __str__(self) -> str:
        return f"Step {self.order}"


class Nutrition(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, related_name="nutrition")
    calories = models.PositiveIntegerField(default=0)
    protein_g = models.DecimalField(max_digits=6, decimal_places=1, default=Decimal("0.0"))
    carbs_g = models.DecimalField(max_digits=6, decimal_places=1, default=Decimal("0.0"))
    fat_g = models.DecimalField(max_digits=6, decimal_places=1, default=Decimal("0.0"))

    def __str__(self) -> str:
        return f"Nutrition for {self.recipe.title}"
