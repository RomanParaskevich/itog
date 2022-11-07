from ..models.reasons import Reasons
from django.contrib import admin


class ReasonsInline(admin.TabularInline):
    model = Reasons
    fields = ('reasons_title', 'reasons_number', 'reasons_description', 'recommendation_title_1',
              'recommendation_description_1', 'recommendation_title_2', 'recommendation_description_2',
              'recommendation_title_3', 'recommendation_description_3')
    fk_name = 'home_page'
    extra = 1
