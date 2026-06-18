from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BankTransactionViewSet, SourceTransactionViewSet

router = DefaultRouter()
router.register(r'bank-transactions', BankTransactionViewSet)
router.register(r'source-transactions', SourceTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
