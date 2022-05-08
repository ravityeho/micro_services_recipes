from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# Create your views here.
# @api_view(['GET'])
# def recipes_api(request):
#     url="http://www.themealdb.com/api/json/v1/1/search.php?f=a"
#     data_response = requests.get(url)
#     return Response(data_response.json())

@api_view(['GET'])
def drinks_recipes(request):
    url="https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    data_response = requests.get(url)
    drinks_data = data_response.json()
    data_response_1 = drinks_data["drinks"]
    return Response(data_response_1)

@api_view(['GET'])
def food_facts(request):
    url="https://world.openfoodfacts.org/api/v0/product/737628064502.json"
    data_response = requests.get(url)
    food_facts = data_response.json()
    # data_response_1 = food_facts["drinks"]
    return Response(food_facts)

