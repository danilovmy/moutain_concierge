from django.db import models


class Booking(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Черновик'
        CONFIRMED = 'confirmed', 'Подтверждена'
        COMPLETED = 'completed', 'Выполнена'
        CANCELED = 'canceled', 'Отменена'
        NO_SHOW = 'no_show', 'No-show'

    created_at = models.DateTimeField(auto_now_add=True)
    lead = models.ForeignKey('leads.Lead', on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=255)

    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=16, choices=Status.choices, default=Status.DRAFT)

    def __str__(self) -> str:
        return f"Бронь #{self.pk} для {self.guest_name}"

    @property
    def total_guest_price(self):
        return sum((item.guest_price or 0) for item in self.items.all())

    @property
    def total_commission(self):
        return sum((item.commission or 0) for item in self.items.all())


class BookingItem(models.Model):
    class ServiceType(models.TextChoices):
        INSTRUCTOR = 'instructor', 'Инструктор'
        RENTAL = 'rental', 'Прокат'
        TAXI = 'taxi', 'Такси'
        NANNY = 'nanny', 'Няня'
        SPA = 'spa', 'SPA'
        OTHER = 'other', 'Другое'

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='items')
    service_type = models.CharField(max_length=32, choices=ServiceType.choices)
    partner = models.ForeignKey('partners.Partner', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    guest_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    commission = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text='Наша комиссия')

    def __str__(self) -> str:
        return f"{self.get_service_type_display()} — {self.description or ''}"
