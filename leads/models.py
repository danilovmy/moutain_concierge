from django.db import models


class Lead(models.Model):
    class SourceType(models.TextChoices):
        HOTEL = 'hotel', 'Отель'
        RENTAL = 'rental', 'Прокат'
        TAXI = 'taxi', 'Такси'
        SITE = 'site', 'Сайт'
        OTHER = 'other', 'Другое'

    class Status(models.TextChoices):
        NEW = 'new', 'Новый'
        IN_PROGRESS = 'in_progress', 'В работе'
        OFFER = 'offer', 'Офер'
        BOOKED = 'booked', 'Забронировано'
        CANCELED = 'canceled', 'Отменён'
        NO_RESPONSE = 'no_response', 'Нет ответа'

    class Need(models.TextChoices):
        INSTRUCTOR = 'instructor', 'Инструктор'
        RENTAL = 'rental', 'Прокат'
        SKIPASS = 'skipass', 'Скипасс'
        HOTEL = 'hotel', 'Отель'
        TAXI = 'taxi', 'Такси'
        NANNY = 'nanny', 'Няня'
        SPA = 'spa', 'SPA'
        OTHER = 'other', 'Другое'

    created_at = models.DateTimeField(auto_now_add=True)
    guest_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, help_text='Телефон/WhatsApp')

    source_type = models.CharField(max_length=32, choices=SourceType.choices)
    source_text = models.CharField(max_length=255, blank=True)

    needs = models.JSONField(default=list, help_text='Список нужд (массив значений Need)')

    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=32, choices=Status.choices, default=Status.NEW)
    comment = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.guest_name} ({self.get_status_display()})"
