from django.contrib import admin
from .models import Employee, Computer, Laptop, Monitor, Printer, Toner, Drum, TonerRequest, DrumRequest

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'mobile', 'email')
    list_filter = ('first_name', 'last_name')

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'user', 'mac_address')
    list_filter = ('user', 'model')

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'user')
    list_filter = ('user', 'model')

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'user')
    list_filter = ('user', 'model')

class PrinterAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'toner', 'drum', 'user')
    list_filter = ('user', 'model')
    search_fields = ['manufacturer', 'model', 'toner', 'drum', 'user', 'mac_address']

class TonerAdmin(admin.ModelAdmin):
    list_display = ('model', 'quantity')
    list_filter = ('model', 'manufacturer')
    search_fields = ['model', ]

class DrumAdmin(admin.ModelAdmin):
    list_display = ('model', 'quantity')
    list_filter = ('model', 'manufacturer')
    search_fields = ['model', ]

class TonerRequestAdmin(admin.ModelAdmin):
    list_display = ('cartridge_name', 'quantity', 'date_created')
    list_filter = ('date_created', 'cartridge_name')
    search_fields = ['date_created', 'cartridge_name']

class DrumRequestAdmin(admin.ModelAdmin):
    list_display = ('drum_name', 'quantity', 'date_created')
    list_filter = ('date_created', 'drum_name')
    search_fields = ['date_created', 'drum_name']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Printer, PrinterAdmin)
admin.site.register(Toner, TonerAdmin)
admin.site.register(Drum, DrumAdmin)
admin.site.register(TonerRequest, TonerRequestAdmin)
admin.site.register(DrumRequest, DrumRequestAdmin)
