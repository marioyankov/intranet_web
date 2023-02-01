from django.urls import path
from app.views import index, employees, computers, printers, toners, drums, RequestAddView

urlpatterns = [
    path('', index, name='index'),
    path('employees/', employees, name='employees'),
    path('computers/', computers, name='computers'),
    path('printers/', printers, name='printers'),
    path('toners/', toners, name='toners'),
    path('drums/', drums, name='drums'),
    path('toner-requests/', RequestAddView.as_view(), name='toner requests'),
]
