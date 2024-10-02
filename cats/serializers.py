from rest_framework import serializers
from cats.models import Cats


class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cats
        fields = (
            'cat_name', 'cat_age', 'cat_gender',
            'cat_breed', 'cat_color', 'cat_details',
            'cat_image', 'cat_points'
        )
        read_only_fields = ['cat_created',]


class GetCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cats
        fields = (
            'cat_name', 'cat_age', 'cat_gender',
            'cat_breed', 'cat_color', 'cat_details',
            'cat_image', 'cat_points'
        )
