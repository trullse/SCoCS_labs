import pytest
from django.test import Client
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from pharmacy.models import \
    Sale, \
    PharmacyDepartment, \
    MedicineCategory, \
    Medicine, \
    Supplier \


@pytest.fixture(scope="function")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        # create any initial data required
        pass


@pytest.fixture(scope='function')
def admin_client(django_db_setup):
    client = Client()
    user = User.objects.create_user(
        username='alx',
        email='alx@admin.com',
        password='password',
        is_superuser=True
    )
    client.force_login(user)
    return client


@pytest.fixture(scope='function')
def user_client(django_db_setup):
    client = Client()
    user = User.objects.create_user(
        username='user',
        email='user@user.com',
        password='password',
        is_superuser=False
    )
    return client


@pytest.fixture
def ph_department(db) -> PharmacyDepartment:
    return PharmacyDepartment.objects.create(address='Minsk')


@pytest.fixture
def supplier(db) -> Supplier:
    return Supplier.objects.create(name='sup')


@pytest.fixture
def category(db) -> MedicineCategory:
    return MedicineCategory.objects.create(name='cat')


@pytest.fixture
def medicine(db, supplier, category) -> Medicine:
    return Medicine.objects.create(name='first',
                                   instruction='eat',
                                   description='good',
                                   price=10,
                                   supplier=supplier,
                                   category=category)


@pytest.fixture
def sale(db, ph_department) -> Sale:
    return Sale.objects.create(ph_department=ph_department, date=timezone.now())
