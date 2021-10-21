from django.db import models
from django.db.models.deletion import CASCADE

# Vendor
class Vendor(models.Model):
    full_name = models.CharField(max_length=50)
    photo= models.ImageField(upload_to="vendor/")
    adress= models.TextField()
    mobile= models.CharField(max_length=15)
    status= models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='1. Vendors'

    def __str__(self):
        return self.full_name

# Unit
class Unit(models.Model):
    title=models.CharField(max_length=50)
    short_name=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural='2. Units'

    def __str__(self):
        return self.title


# Product
class Product(models.Model):
    title=models.CharField(max_length=50)
    detail=models.TextField()
    unit=models.ForeignKey(Unit, on_delete=models.CASCADE)
    photo= models.ImageField(upload_to="product/")

    class Meta:
        verbose_name_plural='3. Products'

    def __str__(self):
        return self.title


# Purchase
class Purchase(models.Model):
    product= models.ForeignKey(Product, on_delete=CASCADE)
    vendor= models.ForeignKey(Vendor, on_delete=CASCADE)
    quantity= models.FloatField()
    price= models.FloatField()
    total_amount= models.FloatField()
    pur_date= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='4. Purcharses'

    def __str__(self):
        return self.product

# Sale
class Sale(models.Model):
    product= models.ForeignKey(Product, on_delete=CASCADE)
    quantity= models.FloatField()
    price= models.FloatField()
    total_amount= models.FloatField()
    sale_date= models.DateTimeField(auto_now_add=True)

    costumer_name= models.CharField(max_length=50, blank=True)
    costumer_mobile= models.CharField(max_length=50)
    costumer_adress= models.TextField()

    class Meta:
        verbose_name_plural='5. Sales'

    

# Inventory
class Inventory(models.Model):
    product= models.ForeignKey(Product, on_delete=CASCADE)
    purcharse= models.ForeignKey(Purchase, on_delete=CASCADE, default=0)
    sale= models.ForeignKey(Sale, on_delete=CASCADE, default=0)
    pur_quantity= models.FloatField( default=0)
    sale_quantity= models.FloatField( default=0)
    total_balance_quantity= models.FloatField()


    class Meta:
        verbose_name_plural='6. Inventory'


    

    