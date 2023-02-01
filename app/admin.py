from django.contrib import admin
from .models import Employee, Computer, Laptop, Monitor, Printer, Toner, Drum, Request

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'mobile', 'email')

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'user', 'mac_address')

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'user')

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'user')

class PrinterAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'toner', 'drum', 'user')

class TonerAdmin(admin.ModelAdmin):
    list_display = ('model', 'quantity')

class DrumAdmin(admin.ModelAdmin):
    list_display = ('model', 'quantity')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Printer, PrinterAdmin)
admin.site.register(Toner, TonerAdmin)
admin.site.register(Drum, DrumAdmin)
admin.site.register(Request)
