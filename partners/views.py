from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Partner


class PartnerListView(LoginRequiredMixin, ListView):
    model = Partner
    paginate_by = 20
    ordering = ["name"]


class PartnerCreateView(LoginRequiredMixin, CreateView):
    model = Partner
    fields = [
        "type",
        "name",
        "phone",
        "whatsapp",
        "email",
        "region",
        "comment",
        "status",
    ]
    success_url = reverse_lazy("partners:list")


class PartnerUpdateView(LoginRequiredMixin, UpdateView):
    model = Partner
    fields = [
        "type",
        "name",
        "phone",
        "whatsapp",
        "email",
        "region",
        "comment",
        "status",
    ]
    success_url = reverse_lazy("partners:list")
