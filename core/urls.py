from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, BankAccountViewSet, BankViewSet, BranchViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'bank-accounts', BankAccountViewSet)
router.register(r'banks', BankViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
