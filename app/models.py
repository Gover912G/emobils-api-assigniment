from django.db import models


# Create your models here.


class Mitbrand(models.Model):
    productName = models.CharField(max_length=50)
    price = models.PositiveIntegerField(max_length=6)
    description = models.TextField(default='Description')
    image = models.ImageField(upload_to='products', default='product.png')

    def __int__(self):
        return self.productName
