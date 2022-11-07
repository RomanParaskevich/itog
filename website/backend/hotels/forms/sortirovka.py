from django.forms import ModelForm
from ..models.hotel_page import HotelPage


class SortirovkaForm(ModelForm):
    class Meta:
        model = HotelPage
        fields = ['swimming_pool', 'parking', 'wi_fi', 'hotel_type', 'min_price']

