from django.db import models

# Vendor
class Vendor(models.Model):
    full_name = models.CharField(max_length=50)
    photo= models.ImageField(upload_to="vendor/")
    adress= models.TextField()
    mobile= models.CharField(max_length=15)
    status= models.BooleanField(default=False)

    def __str__(self):
        return self.full_name