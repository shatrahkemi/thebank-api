from django.contrib import admin
from django.urls import path
from myapp import views
from . views import AccountDetailAPIView ,TransactionListCreateAPIView ,TransferFundsAPIView

urlpatterns = [
     path('admin/', admin.site.urls),
    path('account/<int:pk>/', AccountDetailAPIView.as_view(), name='account-detail'),
    path('transactions/', TransactionListCreateAPIView.as_view(), name='transaction-list'),
    path('transfer/', TransferFundsAPIView.as_view(), name='transfer-funds'),
]

