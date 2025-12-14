from django.db import models


class Partner(models.Model):
    class PartnerType(models.TextChoices):
        INSTRUCTOR = 'instructor', 'Инструктор'
        RENTAL = 'rental', 'Прокат'
        HOTEL = 'hotel', 'Отель'
        TAXI = 'taxi', 'Такси'
        NANNY = 'nanny', 'Няня'
        SPA = 'spa', 'SPA'
        OTHER = 'other', 'Другое'

    class Status(models.TextChoices):
        ACTIVE = 'active', 'Активен'
        PAUSED = 'paused', 'На паузе'

    type = models.CharField(max_length=32, choices=PartnerType.choices)
    name = models.CharField(max_length=255, verbose_name='Название/ФИО')
    phone = models.CharField(max_length=64, blank=True)
    whatsapp = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    region = models.CharField(max_length=255, verbose_name='Курорт/Регион', blank=True)
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.get_type_display()}: {self.name}"
