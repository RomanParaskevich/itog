from django.contrib import admin
from ..models.bron import Bron


@admin.register(Bron)
class BronAdmin(admin.ModelAdmin):
    list_display = ('date_in', 'date_out', 'adults', 'kids')
