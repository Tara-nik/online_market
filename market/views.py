from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django.contrib import messages
from datetime import datetime, timedelta

from decimal import Decimal
from math import *

from .models import User,Goods, Delivery, Order


# Create your views here.


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "your_pizza/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "market/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "market/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "market/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "market/register.html")


def index(request):
    goods = Goods.objects.all()
    return render(request, 'market/index.html', {'goods': goods})


@csrf_exempt
def add_credit(request):
    if request.method == 'POST':
        credit_amount = int(request.POST.get('credit_amount', 0))

        if request.user.is_authenticated:
            request.user.credit_user += credit_amount
            request.user.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, 'market/add_credit.html')


def goods(request):
    goods_list = Goods.objects.all()

    items_per_page = 9
    page = request.GET.get('page', 1)
    paginator = Paginator(goods_list, items_per_page)

    try:
        goods_s = paginator.page(page)
    except PageNotAnInteger:
        goods_s = paginator.page(1)
    except EmptyPage:
        goods_s = paginator.page(paginator.num_pages)

    return render(request, 'market/goods.html', {'goods_s': goods_s})

def delivery_time(request):
    # present_time = datetime.now()
    #
    # delivery_times = [
    #     present_time + timedelta(days=1),
    #     present_time + timedelta(days=3),
    #     present_time + timedelta(days=7),
    # ]
    deliverys = Delivery.objects.all()


    # delivery_info = [
    #     {"time": deliverys.time, "delivery_price": price.deliverys}
    #     for time, price in zip(time, delivery_prices)
    # ]

    return render(request, 'market/delivery.html', {'deliverys': deliverys})


def add_to_cart(request, goods_id=None, delivery_id=None):
    if goods_id is not None:
        # Handle goods addition logic
        goods = get_object_or_404(Goods, pk=goods_id)
        selected_goods = request.session.get('selected_goods', [])
        selected_goods.append(goods.serialize())
        request.session['selected_goods'] = selected_goods
        messages.success(request, f"{goods.name} added to cart.")
    if delivery_id is not None:
        delivery = get_object_or_404(Delivery, pk=delivery_id)
        selected_delivery = request.session.get('selected_delivery', [])
        selected_delivery.append(delivery.serialize())
        request.session['selected_delivery'] = selected_delivery
        messages.success(request, f"{delivery.time} delivery added to cart.")

        # Redirect to the order detail page or another appropriate page
    return HttpResponse(status=204)
def order_detail(request):
    selected_goods = request.session.get('selected_goods', [])
    selected_delivery = request.session.get('selected_delivery', [])

    goods_price = sum(Decimal(goods['price']) for goods in selected_goods)

    delivery_price = sum(Decimal(delivery['delivery_price']) for delivery in selected_delivery)

    total_price = delivery_price + goods_price

    context = {'selected_goods': selected_goods, 'total_price': total_price,
               'selected_delivery': selected_delivery}

    return render(request, 'market/order_detail.html', context)


def reset_order(request):
    request.session.pop('selected_goods', None)
    request.session.pop('selected_delivery', None)

    return redirect('index')


def delete_goods(request, goods_id):
    selected_goods = request.session.get('selected_goods', [])

    index_to_remove = next(
        (index for index, goods in enumerate(selected_goods) if goods['id'] == goods_id), None)

    if index_to_remove is not None:
        del selected_goods[index_to_remove]
        request.session['selected_ingredient'] = selected_goods
        messages.success(request, "Goods removed from cart.")
    else:
        messages.error(request, "Goods not found.")

    return redirect('order_detail')


def delete_delivery(request, time):
    selected_delivery = request.session.get('selected_delivery', [])

    index_to_remove = next(
        (index for index, delivery in enumerate(selected_delivery) if delivery['time'] == time), None)

    if index_to_remove is not None:
        del selected_delivery[index_to_remove]
        request.session['selected_delivery'] = selected_delivery
        messages.success(request, "Delivery removed from cart.")
    else:
        messages.error(request, "Choose the time of the delivery to remove.")

    return redirect('order_detail')


@login_required
def order_checkout(request):
    selected_goods = request.session.get('selected_goods', [])
    selected_delivery = request.session.get('selected_delivery', [])

    goods_price = sum(Decimal(goods['price']) for goods in selected_goods)
    delivery_price = sum(Decimal(delivery['delivery_price']) for delivery in selected_delivery)
    total_price = delivery_price + goods_price

    if request.user.credit_user >= total_price:
        request.user.credit_user -= total_price
        request.user.save()

        request.session.pop('selected_goods', None)
        request.session.pop('selected_delivery', None)

        messages.success(request, "Order placed successfully. Your credit has been deducted.")
        return redirect('index')
    else:
        messages.error(request, "Insufficient credit. Please add credit to your account.")
        return redirect('add_credit')


