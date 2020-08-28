from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('second', views.second, name='second'),
    path('add_user', views.add_user, name='add_user'),
    path('search', views.search, name='search'),
    path('zonefn', views.zonefn, name='zonefn'),
    path('<int:pk>', views.zone_detail , name='zoneds'  )

]
urlpatterns = format_suffix_patterns(urlpatterns)