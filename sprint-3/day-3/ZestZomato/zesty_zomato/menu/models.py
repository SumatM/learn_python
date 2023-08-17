from django.db import models

# Create your models here.

from django.db import models

class Dish(models.Model):
    class Meta:
        app_label = 'menu'
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.dish_name

class Order(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='received')

    def __str__(self):
        return f"{self.customer_name}'s order: {self.dish}"
