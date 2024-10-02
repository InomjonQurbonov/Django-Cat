from django_filters import rest_framework as filters
from cats.models import Cats


class CatsFilter(filters.FilterSet):
    class Meta:
        model = Cats
        fields = [
            'cat_name', 'cat_breed', 'cat_age',
            'cat_gender', 'cat_color', 'cat_created_at',
            'cat_created_at', 'cat_points'
        ]

