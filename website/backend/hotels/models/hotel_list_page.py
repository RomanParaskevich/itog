from django.db import models
from garpix_page.models import BaseListPage
from ..forms.sortirovka import SortirovkaForm


class HotelListPage(BaseListPage):
    paginate_by = 1
    template = 'pages/hotel_list.html'

    def get_context(self, request=None, *args, **kwargs):
        filter_map = {}
        request_list = ('swimming_pool', 'parking', 'wi_fi', 'hotel', 'motel', 'apartments', 'min_price', 'max_price')
        for item in request_list:
            if request.GET.get(item) is not None and request.GET.get(item) != '':
                filter_map[item] = request.GET.get(item)
        for item in filter_map:
            if filter_map[item] == 'on':
                filter_map[item] = True

        context = super().get_context(request, *args, **kwargs)

        if request.GET != {}:
            object_list = self.children.filter(is_active=True)

        return context

    class Meta:
        verbose_name = "HotelList"
        verbose_name_plural = "HotelLists"
        ordering = ('-created_at',)
