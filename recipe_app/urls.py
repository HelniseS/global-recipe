# recipe_app/urls.py
from django.urls import path
from . import views

app_name = "recipe_app"


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/add/', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/mine/', views.MyRecipesView.as_view(), name='my_recipes'),
    path('recipes/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),

]