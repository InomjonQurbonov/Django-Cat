from django.contrib import admin
from cats.models import Cats


class AdminCats(admin.ModelAdmin):
    list_display = ('cat_name', 'cat_breed', 'cat_age', 'cat_points')
    list_filter = ('cat_breed', 'cat_age', 'cat_gender', 'cat_color', 'cat_points')
    search_fields = ('cat_name', 'cat_age', 'cat_gender', 'cat_breed', 'cat_color', 'cat_details', 'cat_points')


admin.site.register(Cats, AdminCats)
