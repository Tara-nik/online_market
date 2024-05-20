from django.urls import path
from django.http import HttpResponseNotFound

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('add_credit/', views.add_credit, name='add_credit'),
    path('goods/', views.goods, name='goods'),
    path('add_to_cart/goods/<int:goods_id>/', views.add_to_cart, name='add_to_cart_goods'),
    path('add_to_cart/delivery/<int:delivery_id>/', views.add_to_cart, name='add_to_cart_delivery_time'),
    path('delivery_time/', views.delivery_time, name='delivery_time'),
    path('order_detail/', views.order_detail, name='order_detail'),
    path('delete_goods/<int:goods_id>/', views.delete_goods, name='delete_goods'),
    path('delete_delivery/<str:time>/', views.delete_delivery, name='delete_delivery'),
    path('order_checkout/', views.order_checkout, name='order_checkout'),
    path('reset_order/', views.reset_order, name='reset_order'),
    path('favicon.ico/', lambda x: HttpResponseNotFound()),


]