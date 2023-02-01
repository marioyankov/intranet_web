from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import RequestFormSet
from .models import Employee, Computer, Laptop, Monitor, Printer, Toner, Drum, Request

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

def toners(request):
    toners = Toner.objects.all()

    context = {
        'toners': toners,
    }

    return render(request, 'toners.html', context)

def drums(request):
    drums = Drum.objects.all()

    context = {
        'drums': drums,
    }

    return render(request, 'drums.html', context)

class RequestAddView(TemplateView):
    template_name = "toner_requests.html"

    def get(self, *args, **kwargs):
        formset = RequestFormSet(queryset=Request.objects.none())
        return self.render_to_response({'request_formset': formset})
    
    def post(self, *args, **kwargs):
        formset = RequestFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("toners"))
        
        return self.render_to_response({'request_formset': formset})