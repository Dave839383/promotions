from django.db import models

# Create your models here.
class PromotionLog(models.Model):
    STATUS_WON = 1
    STATUS_LOST = 0

    STATUS_CHOICES = (
        (STATUS_WON, 'won'),
        (STATUS_LOST, 'lost'),
    )

    CODE_CHOICES = (
        ('ZVLJCYTG', 'ZVLJCYTG'),
        ('AC4ICZFM', 'AC4ICZFM'),
        ('2PKFJHPY', '2PKFJHPY'),
        ('GF2GY8ZF', 'GF2GY8ZF'),
        ('XH4Z5946', 'XH4Z5946'),
    )
    code = models.CharField(
        max_length=9,
        null=False,
        blank=False,
        choices=CODE_CHOICES,
    )

    first_name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    created = models.DateTimeField(
        null=False,
        blank=False,
        auto_now_add=True,
    )

    status = models.IntegerField(
        null=True,
        blank=True,
        choices=STATUS_CHOICES
    )
