from django.urls import path

from . import views


app_name = 'reports'

urlpatterns = [
    path('partner/', views.partner_report, name='partner_report'),
]

