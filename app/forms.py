from django import forms
from django.forms import modelformset_factory, ModelForm
from .models import TonerRequest, DrumRequest, Toner, Drum


TONER_CHOICES = (Toner.objects.values_list('model','model'))
DRUM_CHOICES = (Drum.objects.values_list('model','model'))

TonerRequestFormSet = modelformset_factory(
    TonerRequest,
    fields=("cartridge_name", "quantity"),
    extra=1,
)

DrumRequestFormSet = modelformset_factory(
    DrumRequest,
    fields=("drum_name", "quantity"),
    extra=1,
)

TonerSupplyFormSet = modelformset_factory(
    Toner,
    fields=("model", "quantity"),
    extra=1,

    widgets={
        'model': forms.Select(choices=TONER_CHOICES),
    }
)

DrumSupplyFormSet = modelformset_factory(
    Drum,
    fields=("model", "quantity"),
    extra=1,

    widgets={
        'model': forms.Select(choices=DRUM_CHOICES),
    }
)