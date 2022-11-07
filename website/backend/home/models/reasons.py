from django.db import models
from .home_page import HomePage


class Reasons(models.Model):
    reasons_title = models.CharField(max_length=100)
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, verbose_name='Страница (привязка)',
                                  related_name='reasons_items', null=True)
    reasons_number = models.IntegerField(null=True)
    reasons_description = models.TextField()
    recommendation_title_1 = models.CharField(max_length=100, blank=True, null=True)
    recommendation_description_1 = models.TextField(blank=True, null=True)
    recommendation_title_2 = models.CharField(max_length=100, blank=True, null=True)
    recommendation_description_2 = models.TextField(blank=True, null=True)
    recommendation_title_3 = models.CharField(max_length=100, blank=True, null=True)
    recommendation_description_3 = models.TextField(blank=True, null=True)
