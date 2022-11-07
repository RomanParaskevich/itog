from ..models.home_page import HomePage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin
from .reasons import ReasonsInline


@admin.register(HomePage)
class HomePageAdmin(BasePageAdmin):
    inlines = (ReasonsInline,)
