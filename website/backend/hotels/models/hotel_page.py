from django.db import models
from garpix_page.models import BasePage


class HotelPage(BasePage):
    TYPE = [
        ('Гостиница', 'Гостиница'),
        ('Мотель', 'Мотель'),
        ('Апартаменты', 'Апартаменты'),
    ]
    STARS = [
        ('<li></li>', '1 звезда'),
        ('<li></li><li></li>', '2 звезды'),
        ('<li></li><li></li><li></li>', '3 звезды'),
        ('<li></li><li></li><li></li><li></li>', '4 звезды'),
        ('<li></li><li></li><li></li><li></li><li></li>', '5 звезд'),

    ]
    image = models.ImageField(null=True)
    min_price = models.CharField(max_length=50, null=True)
    max_price = models.CharField(max_length=50, null=True)
    hotel_type = models.CharField(max_length=100, choices=TYPE, null=True)
    stars = models.CharField(max_length=100, choices=STARS, null=True)
    rating = models.FloatField(null=True)
    swimming_pool = models.BooleanField(null=True)
    parking = models.BooleanField(null=True)
    wi_fi = models.BooleanField(null=True)

    template = "pages/hotel.html"



    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
        ordering = ("-created_at",)
