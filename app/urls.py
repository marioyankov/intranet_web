from django.urls import path
from app.views import index, employees, computers, printers, TonersRequestAddView, DrumsRequestAddView, TonersSupplyView, DrumsSupplyView

urlpatterns = [
    path('', index, name='index'),
    path('employees/', employees, name='employees'),
    path('computers/', computers, name='computers'),
    path('printers/', printers, name='printers'),
    path('toners/', TonersRequestAddView.as_view(), name='toners'),
    path('drums/', DrumsRequestAddView.as_view(), name='drums'),
    path('toners-supply/', TonersSupplyView.as_view(), name='toners supply'),
    path('drums-supply/', DrumsSupplyView.as_view(), name='drums supply'),
]
