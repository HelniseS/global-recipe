from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to GlobalRecipe (recipe_app)")

urlpatterns = [
    path('', home, name='home'),
]
