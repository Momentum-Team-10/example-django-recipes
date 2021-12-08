from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = serializers.SlugRelatedField(read_only=True, many=True, slug_field="tag")

    class Meta:
        model = Recipe
        fields = (
            "pk",
            "author",
            "title",
            "prep_time_in_minutes",
            "cook_time_in_minutes",
            "tags",
            "public",
            "favorited_by",
            "tags",
        )
