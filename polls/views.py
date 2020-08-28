from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import userss, zone


# Create your views here.

def index(request):
    return render(request, "first.html")


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
    kuser = request.POST.get('user')
    desc = request.POST.get('desc')
    agree = request.POST.get('agree')
    zone.objects.create(user=kuser, description=desc, agreement_template=agree)
    return redirect('second')
