from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from datetime import datetime
from travel.models import site , gthoteltime , gtsitactivity, gtsiteapparel,gtsiteother,gtsiterestaurant, gtsiteshop
from travel.models import kthoteltime,ktsiteactivity,ktsiteapparel,ktsiteother,ktsiterestaurant,ktsiteshop
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Testmap(request):
    Site = site.objects.get(ID='s7')
    HotelTime = gthoteltime.objects.all()
    Activity = gtsitactivity.objects.all()
    Apparel = gtsiteapparel.objects.all()
    OtherSite = gtsiteother.objects.all()
    Restaurant = gtsiterestaurant.objects.all()
    Shop = gtsiteshop.objects.all()
    return render(request, "testmap.html", locals())

def index(request):
    Site = site.objects.get(ID='s7')
    HotelTime = gthoteltime.objects.all()
    Activity = gtsitactivity.objects.all()
    Apparel = gtsiteapparel.objects.all()
    OtherSite = gtsiteother.objects.all()
    Restaurant = gtsiterestaurant.objects.all()
    Shop = gtsiteshop.objects.all()
    return render(request, "index.html", locals())

def first(request):
    Site = site.objects.get(ID='s7')
    HotelTime = gthoteltime.objects.all()
    Activity = gtsitactivity.objects.all()
    Apparel = gtsiteapparel.objects.all()
    OtherSite = gtsiteother.objects.all()
    Restaurant = gtsiterestaurant.objects.all()
    Shop = gtsiteshop.objects.all()
    return render(request, "first.html", locals())


def New(request):
    Site = site.objects.get(ID='s7')
    #hoteltime
    a = gthoteltime.objects.all()
    HotelTime = a[:50]
    #######
    ac = gtsitactivity.objects.all().order_by('-Score')
    Activity = ac[:9]
    #######
    ap = gtsiteapparel.objects.all().order_by('-Score')
    Apparel = ap[1]
    ######
    ot = gtsiteother.objects.all().order_by('-Score')
    OtherSite = ot[:5]
    ############
    r = gtsiterestaurant.objects.all().order_by('-Score')
    Restaurant = r[:20]
    ###########
    s = gtsiteshop.objects.all().order_by('-Score')
    Shop = s[1]
    return render(request, "new.html", locals())

def Second(request):
    Site = site.objects.get(ID='s8')
    #hoteltime
    a = kthoteltime.objects.all().order_by('Score')
    HotelTime = a[0:100]
    #######
    ac = ktsiteactivity.objects.all().order_by('-Score')
    Activity = ac[:10]
    #######
    ap = ktsiteapparel.objects.all().order_by('-Score')
    Apparel = ap[1]
    ######
    ot = ktsiteother.objects.all().order_by('-Score')
    OtherSite = ot[:5]
    ############
    r = ktsiterestaurant.objects.all().order_by('-Score')
    Restaurant = r[:20]
    ###########
    s = ktsiteshop.objects.all().order_by('-Score')
    Shop = s[1]
    return render(request, "second.html", locals())
