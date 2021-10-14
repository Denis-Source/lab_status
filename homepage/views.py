from django.views.generic import TemplateView
from part.models import Part


class HomePageView(TemplateView):
    template_name = "homepage.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     parts = Part.objects.all()
    #     context["parts"] = parts
