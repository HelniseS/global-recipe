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

title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=220)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(blank=True)
    cooking_time_min = models.PositiveIntegerField(default=0)
    servings = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='recipe_images/', blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  
    tags = models.ManyToManyField(Tag, blank=True, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:60]
            self.slug = base


 i = 1
            while Recipe.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base}-{i}"
                i += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Nutrition(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, related_name='nutrition')
    calories = models.PositiveIntegerField(default=0)
    protein_g = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    carbs_g = models.DecimalField(max_digits=6, decimal_places=1, default=0)
    fat_g = models.DecimalField(max_digits=6, decimal_places=1, default=0)

def __str__(self):
        return f"Nutrition for {self.recipe.title}"


        class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    text = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.text


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    order = models.PositiveIntegerField()
    text = models.TextField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Step {self.order}"