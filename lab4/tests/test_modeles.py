from datetime import datetime

import pytest

from django.utils import timezone
from pharmacy.models import \
    Sale, \
    PharmacyDepartment, \
    MedicineCategory, \
    Medicine, \
    Supplier \


@pytest.mark.django_db
def test_create_department():
    address = 'Minsk'
    phdep = PharmacyDepartment.objects.create(address=address)
    assert phdep.address == address


@pytest.mark.django_db
def test_create_sale():
    phdep = PharmacyDepartment.objects.create(address='Minsk')
    date = timezone.now()
    category = Sale.objects.create(date=date, ph_department=phdep)
    assert category.date == date
