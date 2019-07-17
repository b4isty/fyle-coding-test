from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from .models import Branches
from .serializers import BranchSerializer


class BankDetailAPIView(RetrieveAPIView):
    """
    API to get banks details by banks
    """
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Branches.objects.all()
    pagination_class = LimitOffsetPagination
    lookup_url_kwarg = 'ifsc'


class BranchListAPIView(GenericAPIView):
    """
    API to get data filtered by banks and city
    """
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Branches.objects.all()
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        """
        Using get instead of ListModelMixin to
        get filtered queryset paginated
        """
        bank = request.GET.get('bank')
        city = request.GET.get('city')
        if bank and city:
            qs = self.queryset.filter(bank__name__iexact=bank, city__iexact=city)
            page = self.paginate_queryset(queryset=qs)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(qs, many=True)
            return Response(serializer.data)
        return Response({"message": "banks and city must be provided"}, status=status.HTTP_400_BAD_REQUEST)

