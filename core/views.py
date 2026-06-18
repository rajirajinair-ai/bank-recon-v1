from rest_framework import viewsets
from .models import Company, BankAccount, Bank, Branch, Department
from .serializers import CompanySerializer, BankAccountSerializer, BankSerializer, BranchSerializer, DepartmentSerializer
from django.views.generic import TemplateView

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DashboardView(TemplateView):
    template_name = "dashboard.html"
