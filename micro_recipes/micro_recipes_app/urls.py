from django.urls import path, include
from . import views

urlpatterns = [
    path('drinks_recipes', views.drinks_recipes, name='drinks_recipes'),
    path('food_facts', views.food_facts, name='food_facts')
]
