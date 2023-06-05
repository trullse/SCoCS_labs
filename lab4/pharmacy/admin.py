from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Medicine, Supplier, PharmacyDepartment, MedicineCategory, Sale, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee


class UserAdminCustom(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'employee', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', )
    inlines = [EmployeeInline]


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'get_supplier_name')
    list_filter = ('category', 'supplier__name', 'category__name')
    search_fields = ('name', )

    def get_supplier_name(self, obj):
        return obj.supplier.name

    get_supplier_name.short_description = 'Supplier Name'
    get_supplier_name.admin_order_field = 'supplier__name'


class MedicineCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 0


class PharmacyDepartmentsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['address', 'medicines']}),
    ]
    inlines = [EmployeeInline]


class MedicineInline(admin.TabularInline):
    model = Medicine
    extra = 0


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    inlines = [MedicineInline]


class SaleAdmin(admin.ModelAdmin):
    search_fields = ('date', )
    list_display = ('date', 'ph_department')


admin.site.unregister(User)
admin.site.register(User, UserAdminCustom)


admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(PharmacyDepartment, PharmacyDepartmentsAdmin)
admin.site.register(MedicineCategory, MedicineCategoryAdmin)
admin.site.register(Sale, SaleAdmin)
