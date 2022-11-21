from django.db import models


# Create your models here.
class Package(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    package_name = models.CharField(max_length=50, null=True, blank=True)
    package_id = models.CharField(max_length=50, null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)

    delivery_note = models.CharField(max_length=500, null=True, blank=True)
    delivery_status = models.CharField(max_length=50, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)

    date_shiped = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.tracking_number



class Reciever(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name


class Sender(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



