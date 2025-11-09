# recipe_app/urls.py
from django.urls import path
from . import views

app_name = "recipe_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/add/', views.RecipeCreateView.as_view(), name='recipe_add'),
]
