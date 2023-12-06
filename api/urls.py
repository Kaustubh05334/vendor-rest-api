from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet,PurchaseOrderViewSet,acknowledge_purchase_order,vendor_performance

router = DefaultRouter()
router.register('', VendorViewSet)

router1 = DefaultRouter()
router1.register('', PurchaseOrderViewSet)

urlpatterns = [
    path('vendors/', include(router.urls)),
    path('vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),
    path('purchase_orders/', include(router1.urls)),
    path('purchase_orders/<int:po_id>/acknowledge/',acknowledge_purchase_order, name='acknowledge_purchase_order'),
]
