from django import forms

from .models import Goods, Delivery


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['name', 'image', 'price']


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['time','id']