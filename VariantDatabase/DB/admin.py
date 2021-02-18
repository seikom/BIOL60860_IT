from django.contrib import admin
from .models import Patient_data, Variant_data

admin.site.register(Patient_data)
admin.site.register(Variant_data)