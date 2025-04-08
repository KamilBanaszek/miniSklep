from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa produktu")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena (PLN)")

    def __str__(self):
        return f"{self.name} - {self.price} PLN"