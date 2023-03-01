from django.db import models


# Create your models here.
class Package(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    package_name = models.CharField(max_length=50, null=True, blank=True)
    package_id = models.CharField(max_length=50, null=True, blank=True)
    package_img = models.ImageField(blank=True, null=True)

    weight = models.CharField(max_length=50, null=True, blank=True)

    delivery_note = models.CharField(max_length=500, null=True, blank=True)
    delivery_status = models.CharField(max_length=50, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)

    date_shiped = models.DateField(null=True, blank=True)

    map_url = models.URLField(
            default="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d2617.1432452717227!2d2.5469949679616315!3d49.00785970323614!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sparis%20airport!5e0!3m2!1sen!2sng!4v1677688572432!5m2!1sen!2sng",
            null=True, blank=True)

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
