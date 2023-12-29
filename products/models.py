from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length=90)
    categories  = models.CharField(max_length=70, default='kawai')
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    stock       = models.IntegerField()


class ProductImage(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_path  = models.CharField(max_length=255)