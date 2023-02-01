from django.forms import modelformset_factory
from .models import Request

RequestFormSet = modelformset_factory(
    Request,
    fields=("cartridge_name", "quantity"),
    extra=1
)