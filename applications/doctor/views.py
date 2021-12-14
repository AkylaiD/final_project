from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination

from applications.doctor.models import Doctor
from applications.doctor.serializers import DoctorSerializer, DoctorDetailSerializer


class DoctorFilter(rest_framework.FilterSet):
    min_price_per_visit = rest_framework.NumberFilter(field_name='price_per_visit', lookup_expr='gte')
    max_price_per_visit = rest_framework.NumberFilter(field_name='price_per_visit', lookup_expr='lte')
    min_experience = rest_framework.NumberFilter(field_name='work_experience', lookup_expr='gte')
    max_experience = rest_framework.NumberFilter(field_name='work_experience', lookup_expr='lte')

    class Meta:
        model = Doctor
        fields = [
            'department',
            'min_price_per_visit',
            'max_price_per_visit',
            'min_experience',
            'max_experience'
        ]


class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = DoctorFilter
    search_fields = ['name', ]


    def get_serializer_context(self):
        return {'request': self.request}


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
