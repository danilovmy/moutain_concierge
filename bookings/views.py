from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from .forms import BookingForm, BookingItemFormSet
from .models import Booking


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    paginate_by = 20
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset().select_related('lead')
        status = self.request.GET.get('status')
        partner = self.request.GET.get('partner')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        if status:
            qs = qs.filter(status=status)
        if date_from:
            qs = qs.filter(date_from__gte=date_from)
        if date_to:
            qs = qs.filter(date_to__lte=date_to)
        if partner:
            qs = qs.filter(items__partner_id=partner).distinct()
        return qs


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy('bookings:list')

    def get_initial(self):
        initial = super().get_initial()
        lead_id = self.request.GET.get('lead')
        if lead_id:
            initial['lead'] = lead_id
        if lead_id and not self.request.POST:
            # If creating from lead, prefill guest_name from lead
            try:
                from leads.models import Lead
                lead = Lead.objects.get(pk=lead_id)
                initial.setdefault('guest_name', lead.guest_name)
            except Exception:
                pass
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['items_formset'] = BookingItemFormSet(self.request.POST)
        else:
            context['items_formset'] = BookingItemFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        items_formset = context['items_formset']
        if items_formset.is_valid():
            response = super().form_valid(form)
            items_formset.instance = self.object
            items_formset.save()
            return response
        return self.form_invalid(form)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy('bookings:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['items_formset'] = BookingItemFormSet(self.request.POST, instance=self.object)
        else:
            context['items_formset'] = BookingItemFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        items_formset = context['items_formset']
        if items_formset.is_valid():
            response = super().form_valid(form)
            items_formset.instance = self.object
            items_formset.save()
            return response
        return self.form_invalid(form)


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
