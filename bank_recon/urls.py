from django.contrib import admin
from django.urls import path, include
from core.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('', DashboardView.as_view(), name='dashboard'),
]
