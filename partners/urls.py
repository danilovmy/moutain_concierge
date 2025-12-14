from django.urls import path

from . import views


app_name = 'partners'

urlpatterns = [
    path('', views.PartnerListView.as_view(), name='list'),
    path('create/', views.PartnerCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.PartnerUpdateView.as_view(), name='edit'),
]

