from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import json
from django.db.models import F, ExpressionWrapper, fields, Avg

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=8, unique=True)
    on_time_delivery_rate = models.FloatField(blank=True,null=True)
    quality_rating_avg = models.FloatField(blank=True,null=True)
    average_response_time = models.FloatField(blank=True,null=True)
    fulfillment_rate = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=8, unique=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField(encoder=json.JSONEncoder)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number


@receiver(post_save, sender=PurchaseOrder)
def purchase_order_post_save(sender, instance, created, **kwargs):
    if instance.status=="completed":
        num_completed_po = PurchaseOrder.objects.filter(
            status="completed",
            vendor=instance.vendor,
            acknowledgment_date__lte=F('delivery_date')
        ).count()
        num_po = PurchaseOrder.objects.filter(status="completed",vendor=instance.vendor).count()

        average_quality_rating = PurchaseOrder.objects.filter(
                vendor=instance.vendor,
                status="completed"
            ).aggregate(Avg('quality_rating'))['quality_rating__avg']

        average_time_diff = PurchaseOrder.objects.filter(
                vendor=instance.vendor,
                acknowledgment_date__isnull=False
            ).annotate(
                time_diff=ExpressionWrapper(
                    F('acknowledgment_date') - F('issue_date'),
                    output_field=fields.DurationField()
                )
            ).aggregate(
                avg_time_diff=Avg('time_diff')
            )['avg_time_diff']
                    
        tot_po=PurchaseOrder.objects.filter(vendor = instance.vendor).count()
        vendor_instance = Vendor.objects.get(pk=instance.vendor.id)
        vendor_instance.on_time_delivery_rate= num_completed_po/num_po if num_po else 0
        vendor_instance.quality_rating_avg = average_quality_rating
        vendor_instance.average_response_time=average_time_diff.total_seconds()/3600 if average_time_diff else None
        vendor_instance.fulfillment_rate=num_po/tot_po if tot_po else 0
        vendor_instance.save()


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date.strftime('%Y-%m-%d')}"