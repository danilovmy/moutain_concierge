from django import forms
from django.forms import inlineformset_factory

from .models import Booking, BookingItem


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'lead',
            'guest_name',
            'date_from',
            'date_to',
            'status',
        ]


BookingItemFormSet = inlineformset_factory(
    Booking,
    BookingItem,
    fields=['service_type', 'partner', 'description', 'guest_price', 'commission'],
    extra=1,
    can_delete=True,
)

