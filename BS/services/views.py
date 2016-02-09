from django.views import generic
from .models import TypeOfService


class Services(generic.ListView):
    model = TypeOfService
    template_name = "services.html"



