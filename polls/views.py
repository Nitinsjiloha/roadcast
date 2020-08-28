from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response

from polls.serializers import ZoneSerializer
from .models import userss, zone
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

# Create your views here.

def index(request):
    qs = zone.objects.all()
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'zones': paged_listings}
    return render(request, "first.html", context)


def second(request):
    name = userss.objects.all()
    context = {'users': name}
    return render(request, "second.html", context)


@csrf_exempt
def add_user(request):
    name = request.POST.get('user_name')
    userss.objects.create(name=name)
    return redirect('second')


@csrf_exempt
def search(request):
    name = request.POST.get('query')
    values = userss.objects.filter(name__icontains=name)
    paginator = Paginator(values, 4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}
    return render(request, 'second.html', context)


@csrf_exempt
def zonefn(request):
    user_name = request.POST.get('user')
    desc = request.POST.get('desc')
    agree = request.POST.get('agree')
    user_qs = userss.objects.get(name=user_name)
    print(user_qs)
    zone.objects.create(user=user_qs, description=desc, agreement_template=agree)
    return redirect('second')


@api_view(['GET', 'PUT', 'DELETE'])
def zone_detail(request, pk):
    try:
        zones = zone.objects.get(pk=pk)
    except zones.DoesNotExist:
        return JsonResponse({'message': 'The zone does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        zone_serializer = ZoneSerializer(zone)
        return Response(zone_serializer.data)

    elif request.method == 'PUT':
        zone_data = JSONParser().parse(request)
        zone_serializer = ZoneSerializer(zone, data=zone_data)
        if zone_serializer.is_valid():
            zone_serializer.save()
            return JsonResponse(zone_serializer.data)
        return JsonResponse(zone_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     zone.delete()
    #     return JsonResponse({'message': 'zone was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)