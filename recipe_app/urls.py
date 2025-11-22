# recipe_app/urls.py
from django.urls import path
from . import views

app_name = "recipe_app:home"


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/add/', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('recipes/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]