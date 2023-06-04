from django.urls import path

from . import views

app_name = "pharmacy"
urlpatterns = [
    # ex: /pharmacy/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /pharmacy/categories/
    path("categories/", views.CategoriesIndexView.as_view(), name="category_index"),
    # ex: /pharmacy/categories/5/
    path("categories/<int:pk>/", views.CategoriesDetailView.as_view(), name="category_detail"),
    # ex: /pharmacy/medicines/
    path("medicines/", views.MedicinesIndexView.as_view(), name="medicine_index"),
    # ex: /pharmacy/medicines/2/
    path("medicines/<int:pk>/", views.MedicinesDetailView.as_view(), name="medicine_detail"),
    # ex: /pharmacy/sales/
    path("sales/", views.SalesIndexView.as_view(), name="sale_index"),
    # ex: /pharmacy/sales/2/
    path("sales/<int:pk>/", views.SalesDetailView.as_view(), name="sale_detail"),
    # ex: /pharmacy/sales/add/
    path("sales/add/", views.SaleCreate.as_view(), name="sale_add"),
    # ex: /pharmacy/suppliers/
    path("suppliers/", views.SuppliersIndexView.as_view(), name="supplier_index"),
    # ex: /pharmacy/suppliers/2/
    path("suppliers/<int:pk>/", views.SuppliersDetailView.as_view(), name="supplier_detail"),
]
