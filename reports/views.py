from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render

from bookings.models import BookingItem
from partners.models import Partner


@login_required
def partner_report(request):
    partner_id = request.GET.get('partner')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    partners = Partner.objects.all().order_by('name')
    items = BookingItem.objects.select_related('booking', 'partner')

    if partner_id:
        items = items.filter(partner_id=partner_id)
    if date_from:
        items = items.filter(booking__date_from__gte=date_from)
    if date_to:
        items = items.filter(booking__date_to__lte=date_to)

    totals = items.aggregate(
        total_turnover=Sum('guest_price'),
        total_commission=Sum('commission'),
    )

    context = {
        'partners': partners,
        'items': items,
        'selected_partner': int(partner_id) if partner_id else None,
        'date_from': date_from,
        'date_to': date_to,
        'totals': totals,
    }
    return render(request, 'reports/partner_report.html', context)
