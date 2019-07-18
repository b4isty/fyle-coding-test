from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Branches
from .serializers import BranchSerializer


class BankDetailAPIView(ListAPIView):
    """
    API to get banks details by banks
    """
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Branches.objects.all()
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        """
        Return filtered queryset if ifsc provided
        :return:
        """
        conditions = Q()
        ifsc_list = self.request.GET.get('ifsc').split(',')
        for ifsc in ifsc_list:
            conditions |= Q(ifsc__icontains=ifsc)
        qs = self.queryset.filter(conditions)
        return qs


class BranchListAPIView(ListAPIView):
    """
    API to get data filtered by banks and city
    """
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Branches.objects.all()
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        """Return filtered queryset if bank and/or city provided """
        bank_list = self.request.GET.get('bank', '').split(',')
        city_list = self.request.GET.get('city', '').split(',')
        condition1 = Q()
        condition2 = Q()
        qs = self.queryset
        if bank_list or city_list:
            for bank in bank_list:
                condition1 |= Q(bank__name__icontains=bank)
            qs = qs.filter(condition1)
            for city in city_list:
                condition2 |= Q(city__icontains=city)
            qs = qs.filter(condition2)
        return qs