from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import TonerRequestFormSet, DrumRequestFormSet, TonerSupplyFormSet, DrumSupplyFormSet
from .models import Employee, Computer, Laptop, Monitor, Printer, Toner, Drum, TonerRequest, DrumRequest

# Create your views here.

def index(request):

    context = {
        
    }

    return render(request, 'index.html', context)

def employees(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }

    return render(request, 'employees.html', context)

def computers(request):
    computers = Computer.objects.all()
    monitors = Monitor.objects.all()
    laptops = Laptop.objects.all()

    context = {
        'computers': computers,
        'laptops': laptops,
        'monitors': monitors,
    }

    return render(request, 'computers.html', context)

def printers(request):
    printers = Printer.objects.all()
    context = {
        'printers': printers,
    }

    return render(request, 'printers.html', context)

class TonersRequestAddView(TemplateView):
    template_name = "toners.html"

    def get(self, *args, **kwargs):
        
        formset = TonerRequestFormSet(queryset=TonerRequest.objects.none())
        toners = Toner.objects.all()

        context = {
            'toners': toners,
            'request_formset': formset,
        }

        return self.render_to_response(context)
    
    def post(self, *args, **kwargs):
        formset = TonerRequestFormSet(data=self.request.POST)
        toners = Toner.objects.all()

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("toners"))
        
        context = {
            'toners': toners,
            'request_formset': formset,
        }
        
        return self.render_to_response(context)

class DrumsRequestAddView(TemplateView):
    template_name = "drums.html"

    def get(self, *args, **kwargs):
        formset = DrumRequestFormSet(queryset=DrumRequest.objects.none())
        drums = Drum.objects.all()

        context = {
            'drums': drums,
            'request_formset': formset,
        }

        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        formset = DrumRequestFormSet(data=self.request.POST)
        drums = Drum.objects.all()

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("drums"))
        
        context = {
            'drums': drums,
            'request_formset': formset,
        }
        
        return self.render_to_response(context)

class TonersSupplyView(TemplateView):
    template_name = "toners supply.html"
    

    def get(self, *args, **kwargs):
        toner_formset = TonerSupplyFormSet(queryset=Toner.objects.none())

        context = {
            'supply_formset': toner_formset,
        }

        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        toner_formset = TonerSupplyFormSet(data=self.request.POST)

        if toner_formset.is_valid():
            toners = toner_formset.cleaned_data
            for toner in toners:
                curr_toner = Toner.objects.get(model=toner.get('model'))
                curr_toner.quantity += toner.get('quantity')
                curr_toner.save()

            return redirect(reverse_lazy("toners"))
        
        context = {
            'supply_formset': toner_formset,
        }

        return self.render_to_response(context)

class DrumsSupplyView(TemplateView):
    template_name = "drums supply.html"

    def get(self, *args, **kwargs):
        drum_formset = DrumSupplyFormSet(queryset=Toner.objects.none())

        context = {
            'supply_formset': drum_formset,
        }

        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        drum_formset = DrumSupplyFormSet(data=self.request.POST)

        if drum_formset.is_valid():
            drum_formset.save()
            return redirect(reverse_lazy("drums"))
        
        context = {
            'supply_formset': drum_formset,
        }

        return self.render_to_response(context)