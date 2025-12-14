from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .forms import LeadForm
from .models import Lead


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    paginate_by = 20
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.GET.get('status')
        source = self.request.GET.get('source')
        date = self.request.GET.get('date')
        if status:
            qs = qs.filter(status=status)
        if source:
            qs = qs.filter(source_type=source)
        # Simple date filter by created date (YYYY-MM-DD)
        if date:
            qs = qs.filter(created_at__date=date)
        return qs


class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy('leads:list')


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy('leads:list')


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
