from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Supplier(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class MedicineCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=50)
    instruction = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(MedicineCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class PharmacyDepartment(models.Model):
    address = models.CharField(max_length=100)
    medicines = models.ManyToManyField(Medicine)

    class Meta:
        ordering = ["address"]

    def __str__(self):
        return self.address


class Sale(models.Model):
    date = models.DateTimeField("Date sold", default=datetime.now())
    ph_department = models.ForeignKey(PharmacyDepartment, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.date.__str__()

    def clean(self):
        if self.date > timezone.now():
            raise ValidationError("Date is incorrect")


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(PharmacyDepartment, on_delete=models.CASCADE)
