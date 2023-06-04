from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import MedicineCategory, Medicine, Supplier, Sale


class IndexView(generic.TemplateView):
    template_name = "pharmacy/index.html"


class CategoriesIndexView(generic.ListView):
    template_name = "pharmacy/categories_index.html"
    context_object_name = "categories_list"

    def get_queryset(self):
        """
        Return the categories
        """
        return MedicineCategory.objects.order_by("-name")


class CategoriesDetailView(generic.DetailView):
    model = MedicineCategory
    template_name = "pharmacy/categories_detail.html"


class MedicinesIndexView(generic.ListView):
    template_name = "pharmacy/medicines_index.html"
    context_object_name = "medicines_list"

    def get_queryset(self):
        """
        Return the medicines
        """
        return Medicine.objects.order_by("-name")


class MedicinesDetailView(generic.DetailView):
    model = Medicine
    template_name = "pharmacy/medicines_detail.html"


class SalesIndexView(LoginRequiredMixin, generic.ListView):
    template_name = "pharmacy/sales_index.html"
    context_object_name = "sales_list"

    def get_queryset(self):
        """
        Return the sales
        """
        return Sale.objects.order_by("-date")


class SalesDetailView(LoginRequiredMixin, generic.DetailView):
    model = Sale
    template_name = "pharmacy/sales_detail.html"


class SuppliersIndexView(LoginRequiredMixin, generic.ListView):
    template_name = "pharmacy/suppliers_index.html"
    context_object_name = "suppliers_list"

    def get_queryset(self):
        """
        Return the suppliers
        """
        return Supplier.objects.order_by("-name")


class SuppliersDetailView(LoginRequiredMixin, generic.DetailView):
    model = Supplier
    template_name = "pharmacy/suppliers_detail.html"


class SaleCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'pharmacy.add_sale'
    model = Sale
    fields = '__all__'
    initial = {'date': datetime.now(), }
    template_name = "pharmacy/sales_add.html"
    success_url = reverse_lazy('pharmacy:sale_index')
