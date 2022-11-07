from django.db import models
from garpix_page.models import BasePage
from ..forms.bron import BronForm
from garpix_notify.models import Notify
from django.conf import settings


class HomePage(BasePage):
    template = "pages/home.html"

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if request.method == 'POST':
            form = BronForm(request.POST)
            if form.is_valid():
                feedback = form.save()
                Notify.send(settings.FEEDBACK_EVENT, {
                    'feedback': feedback,
                }, )
                context.update({
                    'message': 'Сообщение успешно отправлено',
                })
            context.update({
                'form': form,
            })
        return context

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Homes"
        ordering = ("-created_at",)
