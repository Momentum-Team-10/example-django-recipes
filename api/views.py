from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from core.models import Recipe
from .serializers import RecipeSerializer


class RecipeListView(ListAPIView):
    """
    List all recipes
    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # All this below is cpmmented out because I don't need it now that I am using ListAPIView
    # I DID need it when I was using APIView as my parent class for this view.
    # def get(self, request, format=None):
    #     """
    #     Create a response that includes a list of recipes
    #     """
    #     recipes = Recipe.objects.all()  # queryset
    #     serializer = RecipeSerializer(recipes, many=True)

    #     return Response(serializer.data)


class RecipeDetailView(RetrieveAPIView):
    """
    Get a single recipe
    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
