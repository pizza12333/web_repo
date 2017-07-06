from django.shortcuts import render

# Create your views here.
from rest_api.models import ChickenData
from rest_api.serializers import ChickenSerializer
from rest_framework import filters
from rest_framework import generics
import django_filters

class ChickenFilter(django_filters.FilterSet):

    min_id = django_filters.NumberFilter(name='id', lookup_expr='lte')
    max_id = django_filters.NumberFilter(name='id', lookup_expr='gte')

    date = django_filters.CharFilter(name='date' ,lookup_expr='exact')

    min_year = django_filters.NumberFilter(name='year', lookup_expr='lte')
    max_year = django_filters.NumberFilter(name='year', lookup_expr='gte')

    min_month = django_filters.NumberFilter(name='month', lookup_expr='lte')
    max_month = django_filters.NumberFilter(name='month', lookup_expr='gte')

    min_day = django_filters.NumberFilter(name='day', lookup_expr='lte')
    max_day = django_filters.NumberFilter(name='day', lookup_expr='gte')

    min_day_of_weeks = django_filters.NumberFilter(name='day_of_weeks', lookup_expr='lte')
    max_day_of_weeks = django_filters.NumberFilter(name='day_of_weeks', lookup_expr='gte')

    min_gender = django_filters.NumberFilter(name='gender', lookup_expr='lte')
    max_gender = django_filters.NumberFilter(name='gender', lookup_expr='gte')

    min_age = django_filters.NumberFilter(name='age', lookup_expr='lte')
    max_age = django_filters.NumberFilter(name='age', lookup_expr='gte')

    loc_mid = django_filters.CharFilter(name='loc_mid', lookup_expr='exact')

    min_call = django_filters.NumberFilter(name='call', lookup_expr='lte')
    max_call = django_filters.NumberFilter(name='call', lookup_expr='gte')


    class Meta:
        model = ChickenData
        fields = ['id','date', 'year', 'month', 'day', 'day_of_weeks', 'gender', 'age', 'loc_mid', 'call']



class ChickenViewSet(generics.ListAPIView):
    serializer_class = ChickenSerializer
    queryset = ChickenData.objects.using('open_data').all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ChickenFilter