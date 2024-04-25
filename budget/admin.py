from django.contrib import admin
from .models import Threshold, Transaction, Alert

# Register your models here.
admin.site.register(Threshold)
admin.site.register(Transaction)
admin.site.register(Alert)