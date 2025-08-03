from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import UnifiedProduct, PriceUpdateLog
import threading
_local = threading.local()


@receiver(pre_save, sender=UnifiedProduct)
def set_default_price(sender, instance, **kwargs):
    if instance.price is None:
        instance.price = 0
    if instance.pk:
        _local.old_price = UnifiedProduct.objects.get(pk=instance.pk).price

@receiver(post_save, sender=UnifiedProduct)
def log_price_change(sender, instance, created, **kwargs):
    if (not created and hasattr(_local, 'old_price')) and instance.price != _local.old_price:
        PriceUpdateLog.objects.create(
            product=instance,
            old_price=_local.old_price,
            new_price=instance.price
        )