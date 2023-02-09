from django.urls import path
from app.views import index, employees, computers, printers, drums, TonersRequestAddView

urlpatterns = [
    path('', index, name='index'),
    path('employees/', employees, name='employees'),
    path('computers/', computers, name='computers'),
    path('printers/', printers, name='printers'),
    path('toners/', TonersRequestAddView.as_view(), name='toners'),
    path('drums/', drums, name='drums'),
]
