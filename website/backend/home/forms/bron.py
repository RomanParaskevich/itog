from django.forms import ModelForm
from ..models.bron import Bron


class BronForm(ModelForm):
    class Meta:
        model = Bron
        fields = ['date_in', 'date_out', 'adults', 'kids']
