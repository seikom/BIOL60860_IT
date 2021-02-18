from django.contrib import admin
from .models import Patient, Testvariant, Interpretation

admin.site.register(Patient)
admin.site.register(Testvariant)
admin.site.register(Interpretation)