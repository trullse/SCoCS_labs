from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Medicine, Supplier, PharmacyDepartment, MedicineCategory, Sale, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee


class UserAdminCustom(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', )
    inlines = [EmployeeInline]


admin.site.unregister(User)
admin.site.register(User, UserAdminCustom)


admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(PharmacyDepartment)
admin.site.register(MedicineCategory)
admin.site.register(Sale)
