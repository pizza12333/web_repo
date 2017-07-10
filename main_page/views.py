from django.shortcuts import render
from django.db import connections
from django.db.models import Count, Sum
from django.http import JsonResponse
from rest_api.models import ChickenData

# Create your views here.
def main_template(request):
    return render(request, 'main_page/index.html', {})

def dump2json(request):
    query = ChickenData.objects.using('open_data')
    result_set = query.values('gender').annotate(Sum('call'))
    return JsonResponse(list(result_set), safe=False)

def test_page(request):
    return render(request, 'main_page/test.html', {})

