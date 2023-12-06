from rest_framework import serializers
from .models import Vendor,PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code']
        extra_kwargs = {
            'on_time_delivery_rate': {'read_only': True},
            'quality_rating_avg': {'read_only': True},
            'average_response_time': {'read_only': True},
            'fulfillment_rate': {'read_only': True}
        }

class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(
        queryset=Vendor.objects.all(), source='vendor', write_only=True
    )
    class Meta:
        model = PurchaseOrder
        fields = ['po_number', 'vendor', 'vendor_id', 'order_date', 'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date']

        
class PurchaseOrderAcknowledgmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['acknowledgment_date']