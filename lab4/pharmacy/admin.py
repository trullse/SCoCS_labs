from django.contrib import admin

from .models import Medicine, Supplier, PharmacyDepartment, MedicineCategory, Sale

admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(PharmacyDepartment)
admin.site.register(MedicineCategory)
admin.site.register(Sale)
