from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()


class Cats(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cat_name = models.CharField(max_length=100, blank=True, null=True)
    cat_age = models.IntegerField(blank=True, null=True)
    cat_gender = models.CharField(max_length=100, blank=True, null=True)
    cat_breed = models.CharField(max_length=100, blank=True, null=True)
    cat_color = models.CharField(max_length=100, blank=True, null=True)
    cat_details = models.TextField(blank=True, null=True)
    cat_image = models.ImageField(upload_to='cats/Y%m%d', blank=True, null=True)
    cat_created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    cat_points = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.cat_name if self.cat_name else 'Unnamed Cat'

    class Meta:
        db_table = 'cats'
        verbose_name = 'Cats'
        verbose_name_plural = 'Cats'
