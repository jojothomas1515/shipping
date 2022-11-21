from django.contrib import admin
from django.forms import BaseInlineFormSet
from rest_framework.exceptions import ValidationError

from .models import Package, Reciever, Sender


class SenderInline(admin.StackedInline):
    model = Sender
    max_num = 1

class RecieverInline(admin.StackedInline):
    model = Reciever
    max_num = 1

# Register your models here.
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    inlines = [SenderInline,RecieverInline]

