from django.db import models


class Category(models.Model):
    category    = models.CharField(max_length=50)


    def __str__(self):
        return self.category


    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name        = models.CharField(max_length=90)
    name_detail = models.CharField(max_length=120, default='name')
    categories  = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image_path  = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    stock       = models.IntegerField()
    delivery    = models.BooleanField(default=False)
    collect     = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name}, {self.price}'
    
    def total_quantity_in_carts(self):
        return sum(cart_item.quantity for cart_item in self.cartitem_set.all())


