from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta



# Create your models here.

class User(AbstractUser):
    credit_user = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "credit": self.credit_user,
        }

    def __str__(self):
        return self.username


class Goods(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField(default='https://example.com/placeholder.jpg')
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,
            "price": float(self.price),
        }

    def __str__(self):
        return self.name


class Delivery(models.Model):
    TIME_CHOICES = [
        ('one day', "one day later"),
        ('three days', "three days later"),
        ('seven days', "seven days later"),
    ]

    time = models.CharField(max_length=50, choices=TIME_CHOICES)
    delivery_price = models.DecimalField(max_digits=5, decimal_places=2)

    def serialize(self):
        return {
            "id": self.id,
            "delivery_price": float(self.delivery_price),
            "time": self.get_time_display(),
        }

    def __str__(self):
        return f"{self.get_time_display()} is {self.delivery_price}"
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    goods = models.ManyToManyField(Goods)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order #{self.pk}"


