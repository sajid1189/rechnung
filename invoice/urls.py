from .views import InvoiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', InvoiceViewSet, basename='user')
invoice_router_patterns = router.urls

invoice_patterns = [

] + invoice_router_patterns

