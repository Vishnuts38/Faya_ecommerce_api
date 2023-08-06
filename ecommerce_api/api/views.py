

from django.views.generic.base import TemplateView

from .models import CustomUser

class TableView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = CustomUser.objects.filter(groups__name="user")
        return context