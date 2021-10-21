from django.db import models
from django.db.models.deletion import CASCADE

# Vendor
class Vendor(models.Model):
    full_name = models.CharField(max_length=50)
    photo= models.ImageField(upload_to="vendor/")
    adress= models.TextField()
    mobile= models.CharField(max_length=15)
    status= models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

#Unit
class Unit(models.Model):
    title=models.CharField(max_length=50)
    short_name=models.CharField(max_length=50)

    def __str__(self):
        return self.title


#Product
class Product(models.Model):
    title=models.CharField(max_length=50)
    detail=models.TextField()
    unit=models.ForeignKey(Unit, on_delete=models.CASCADE)
    photo= models.ImageField(upload_to="product/")

    def __str__(self):
        return self.title


#Purcharse
class Purcharse(models.Model):
    product= models.ForeignKey(Product, on_delete=CASCADE)
    vendor= models.ForeignKey(Vendor, on_delete=CASCADE)
    qty= models.FloatField()
    price= models.FloatField()
    total= models.FloatField()
    pur_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product


    

    