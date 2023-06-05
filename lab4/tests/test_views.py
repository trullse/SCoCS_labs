import datetime

import pytest
import uuid

from django.urls import reverse
from django.contrib.auth.models import Group, User, Permission
from django.test import Client
from django.utils import timezone


@pytest.mark.django_db
def test_index_view(user_client: Client):
    url = reverse('pharmacy:index')
    response = user_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_categories_index_view(user_client: Client):
    url = reverse('pharmacy:category_index')
    response = user_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_non_existing_categories_detail_view(user_client: Client):
    url = reverse('pharmacy:category_detail', args=[9])
    response = user_client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_medicines_index_view(user_client: Client):
    url = reverse('pharmacy:medicine_index')
    response = user_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_non_existing_medicines_detail_view(user_client: Client):
    url = reverse('pharmacy:medicine_detail', args=[7])
    response = user_client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_non_employee_suppliers_index_view(user_client: Client):
    url = reverse('pharmacy:supplier_index')
    response = user_client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_non_employee_sales_index_view(user_client: Client):
    url = reverse('pharmacy:supplier_index')
    response = user_client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_employee_sales_index_view(admin_client: Client):
    url = reverse('pharmacy:supplier_index')
    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_employee_sales_add_view(admin_client: Client):
    url = reverse('pharmacy:sale_add')
    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_non_employee_sales_add_view(user_client: Client):
    url = reverse('pharmacy:sale_add')
    response = user_client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_sales_create_allowed(admin_client: Client, ph_department, medicine):
    url = reverse('pharmacy:sale_add')
    response = admin_client.post(url, {'date': datetime.datetime.now(),
                                       'ph_department': ph_department})
    assert response.status_code == 200


@pytest.mark.django_db
def test_sales_create_denies(user_client: Client, ph_department, medicine):
    url = reverse('pharmacy:sale_add')
    response = user_client.post(url, {'date': datetime.datetime.now(),
                                      'ph_department': ph_department})
    assert response.status_code == 302
