from django.urls import path

from .views import BankDetailAPIView, BranchListAPIView

app_name = 'banks'

urlpatterns = [
    path('bank/ifsc/', BankDetailAPIView.as_view(), name='bank_detail'),
    path('branch/', BranchListAPIView.as_view(), name='branches'),
]
